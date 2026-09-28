---
title: "agdog: Seu Monitor Não Sabe o Que É um Agente"
subtitle: "Um monitor de terminal que agrupa CPU, GPU e memória pelo agente dono de cada processo. Escrever uma assinatura nova para ele provou que meu próprio monitor escondia um terço da minha máquina desde julho."
date: 2026-09-27
description: "Lançamento do agdog, um monitor de terminal open source que agrupa recursos pelo agente dono de cada processo, em vez de agrupar por processo ou por dispositivo. As mesmas onze perguntas respondidas por um modelo local e por um hospedado, separados por uma flag, e o bug que uma linha de comando real revelou."
cover: /assets/img/2026-09-27-agdog-launch.png
coverAlt: "Uma vasta grade de blocos de carvão escuro idênticos que some ao longe, com três deles brilhando em âmbar quente por dentro enquanto todos os outros permanecem apagados, luz de contorno em ciano acinzentado nas bordas escuras e brilho suave ao redor dos acesos."
---

Iniciei um modelo na minha própria máquina, abri meu próprio monitor, e a execução não estava lá.

Uma linha guardava tudo que eu não tinha nomeado. 890 processos, 427% de CPU, 21 gigabytes, rotulados como `unassigned`. Em algum lugar ali dentro um modelo de decisão mastigava 400 tickets de suporte, e meu monitor não tinha nada a dizer sobre isso.

Hoje o agdog é público.

## A chave de agrupamento

Todo monitor escolhe uma chave de agrupamento, e a chave é o projeto inteiro.

O `htop` agrupa por processo. O `nvitop` agrupa por dispositivo. Nenhum dos dois está errado. Ambos respondem uma pergunta precisa sobre uma máquina rodando um trabalho por vez.

Minha máquina não roda um trabalho. Agora mesmo ela roda sete sessões de código, um servidor de inferência, e qualquer modelo que um script resolveu carregar. Cada um deles é uma árvore de processos, não um processo. Uma sessão de código é um binário, uma dúzia de filhos em node e alguns servidores MCP.

Então a pergunta que eu tenho nunca é "o que o PID 68715 está fazendo". É "qual agente é dono daqueles 7,5 gigabytes, e ele travou?". Nada na minha máquina respondia isso, porque nada na minha máquina sabia o que era um agente.

## O que você vê

```
$ agdog agents
AGENT                        KIND    STATE    PROC  CPU%    MEM  task
claude:blog                  coding  working    19   27%   0.9G  claude --resume e302a7b9
  ↳ claude:observer-sessions sub     idle                        [process]
claude:stratify              coding  idle       11    3%   0.7G  claude --resume 6840a557
claude:firestore             coding  idle       10    1%   0.3G  claude
laya                         infer   working     1  219%   7.5G  /opt/homebrew/Cellar/pyth
ollama                       infer   idle        1    0%   0.0G  /opt/homebrew/opt/ollama/
unassigned                   unknown working   828  279%  17.8G  /System/Library/Framework
```

Essa é uma captura real com quatro linhas de sessão removidas. Uma linha por agente. Sessões paralelas assumem o nome do diretório do projeto, então `claude:blog` e `claude:stratify` nunca se misturam numa única linha `claude`. Processos filhos entram na sessão que os criou, e um subagente aninha sob o pai com um `↳`. Tudo que não é um agente cai em `unassigned`, escondido até você apertar `a`.

O estado vem da utilização e do tempo de retenção: trabalhando, ocioso, travado quando a memória fica presa sem atividade, desgovernado quando algo satura e sustenta, e encerrado com falha. Travado é o motivo pelo qual construí isso. Uma renderização emperrada segura a memória dela e parece exatamente igual a uma ocupada em qualquer outra ferramenta.

## Separados por uma flag

Aqui está o teste que fechou o argumento.

O `doceval` faz onze perguntas tipadas sobre um documento. A voz está ativa? A abertura é forte? O leitor sai com a ideia principal? Ele aceita uma flag `--backend`, e dois modelos respondem. O Jev é hospedado. O Layla roda na sua máquina a partir de pesos abertos, e o checkpoint inteiro dele tem 3,4 megabytes.

Mesmo documento, mesmas onze perguntas, uma flag entre eles.

```
$ doceval eval --backend laya kubeside-launch.md
  kubeside-launch.md    --    UNSCORED
  ... dez dimensões, todas marcadas para revisão ...
  laya-multilingual · 0 tokens · 9.0s · 0 cached

$ doceval eval --backend jev kubeside-launch.md
  kubeside-launch.md   0.82   GOOD
  ... dez dimensões, duas marcadas para revisão ...
  jev-1.13.0 · 3,179 tokens · 0.6s · 0 cached
```

A execução local não custou nada e não saiu da rede. Ela também não produziu nota aproveitável: o Layla sai confiante demais de fábrica, então toda dimensão ficou abaixo do limiar de confiança e foi marcada para revisão. Ajustar uma temperatura com os seus próprios dados resolve isso, trabalho que o modelo hospedado já fez. Uma execução de cada num único documento não prova nada sobre qual modelo é melhor. Essa nunca foi a pergunta.

A pergunta era onde o trabalho aconteceu. Com `--backend laya`, o agdog mostra `laya infer working 219% 7.5G`. Com `--backend jev`, o agdog não mostra nada, porque nada rodou aqui. Onze perguntas saíram do prédio por HTTPS e voltaram como números.

Um modelo de 3,4 megabytes respondendo perguntas tipadas é [o argumento do modelo superqualificado](/pt-br/posts/2026-06-16-frontier-model-overqualified/) no limite.

## Atribuição é o produto

Três camadas, da mais confiável para a menos.

Uma marca explícita na variável de ambiente `AGENT_ID` ganha de tudo. Exporte ela e o processo é agrupado sob aquele nome, qualquer que seja o nome do binário. Só no Linux, e o motivo vale saber: o macOS se recusa a expor o ambiente de outro processo, mesmo para um pai. A camada é documentada como indisponível lá, em vez de ficar parecendo quebrada.

Abaixo dela, assinaturas de linha de comando. Depois ancestralidade na árvore de processos, para um worker herdar o agente do pai.

É nessa camada do meio que o Layla faltava, então sentei para adicionar. O Layla vem como console script, o que significa que uma execução em venv chama o python com o script como argumento, e o nome do programa é `Python`, não `laya`. Tudo bem. Escrevi um teste com a linha de comando real colada dentro.

Ele falhou.

Não porque a assinatura nova estivesse errada. Porque uma regra acima dela descartava o processo antes. O agdog exclui qualquer coisa sob `.app/Contents/` para que apps Electron e auxiliares de interface nunca se passem por agentes. Um interpretador do Homebrew mora em `.../Python.app/Contents/MacOS/Python`. Todo agente iniciado por python nessa máquina caía em `unassigned` desde julho: Layla, ComfyUI, treinos do kohya, tudo.

Dois meses de uma resposta confiante, completa e errada. O monitor que escrevi para me dizer o que minha máquina estava fazendo escondia um terço dela em silêncio, e só descobri porque colei uma linha de comando real num teste, em vez de uma plausível.

O agdog já se recusa a inventar GPUs que não consegue ler. [Recusar-se a inventar números](/pt-br/posts/2026-06-09-it-never-knows-it-doesnt-know/) acaba sendo a metade fácil. A metade difícil é uma lista que parece completa.

## Não é um painel

Uma tela é um beco sem saída para um orquestrador. Então mudanças de estado também saem como JSON por um socket local, um socket Unix ou um named pipe no Windows, ambos controlados por acesso do sistema operacional e sem nenhuma porta de rede aberta.

```
$ agdog watch
{"kind":"state_changed","agent_id":"claude:stratify","from":"working","to":"idle","ts_secs":9}
{"kind":"state_changed","agent_id":"claude:stratify","from":"idle","to":"working","ts_secs":22}
```

Uma sessão ficando quieta é o caso sem graça. O mesmo formato de linha carrega uma execução travando ou desgovernando, que é o caso que vale conectar. Assine e reaja: mate o processo desgovernado, recoloque o trabalho travado na fila, segure o próximo lote até a VRAM liberar. Sem raspar tela.

## O que está verificado, e o que não está

Onze semanas, 44 commits, um binário Rust sobre ratatui sem nenhuma dependência de instalação. 53 testes passam no macOS.

O macOS é a plataforma que eu uso, então é a que eu confio: atribuição, CPU por core e utilização de GPU via IOKit leem dados reais. No Linux, a atribuição de processo e memória e a marca `AGENT_ID` estão verificadas em máquinas reais. No Windows, a atribuição e o named pipe rodam como testes contra uma máquina real na CI.

A lacuna é hardware. Eu não tenho uma placa NVIDIA. O caminho NVML compila, tem cobertura de testes unitários, e nunca leu uma GPU real sob carga real. Números fabricados aparecem apenas sob `AGDOG_DEMO=1`, e o rodapé os rotula como `mock (simulated)`. Sem GPU legível, o agdog diz isso em vez de desenhar um dispositivo.

Eu fui dono da chave de agrupamento e da regra de nunca inventar um número. O modelo foi dono da estrutura e da execução.

## Experimente

```
brew install dynaum/tap/agdog
agdog
```

MIT, no [GitHub](https://github.com/dynaum/agdog).

Uma coisa ajuda mais que uma estrela. Rode numa máquina com uma placa NVIDIA real sob carga real e me diga se os números de VRAM por processo batem com o `nvidia-smi`. Essa é a única afirmação que não consigo resolver daqui, e uma bancada limpa também não resolveria. Precisa da máquina de verdade, sobrecarregada, de outra pessoa.
