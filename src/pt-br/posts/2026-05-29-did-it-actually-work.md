---
title: "Funcionou de Verdade?"
subtitle: "Trabalhar com IA presume uma saída em que você confia. Este post mede isso. Velocidade virou métrica de vaidade. Confiança é o número que sobrevive, e três métricas de saúde dizem se o loop está funcionando."
date: 2026-05-29
description: "Velocidade é a métrica errada na era da IA. Confiança é a certa. Por que revisar código gerado por IA é uma disciplina, as três métricas de saúde que dizem se o loop funciona (taxa de falha de mudança, taxa de retrabalho, tempo-até-confiança), e por que o operador permanece no loop."
cover: /assets/img/2026-05-29-did-it-actually-work.png
coverAlt: "Uma bancada de oficina escura à noite. Um único objeto finalizado descansa sob uma lanterna âmbar quente. Ao lado dele, um paquímetro traçado por luz de borda ciano fria, no meio de uma medição."
---

O loop de desenvolvimento com IA já é bem compreendido. Faça a spec do trabalho, compartilhe o contexto, rode o pipeline, automatize a operação chata, escale para muitos agentes, construa suas próprias ferramentas. Tudo isso presume a mesma coisa por baixo: uma saída em que você confia. Quase ninguém faz a pergunta que decide se algo daquilo valeu a pena.

Funcionou de verdade?

O loop é rápido. Esse era o ponto. Mas rápido é a metade fácil de medir e a metade errada para comemorar. Um agente entrega dez pull requests numa tarde. O gráfico de throughput sobe. O gráfico mente se metade delas for revertida na semana seguinte.

## Velocidade é o número errado

Por uma década, times mediram entrega por velocidade. Lead time, frequência de deploy, throughput. Esses números funcionavam porque escrever o código era o gargalo, então mover o código mais rápido significava um time mais saudável.

A era da IA quebrou o proxy. Escrever o código não é mais o gargalo. Um modelo produz mais diff por hora do que qualquer time produzia. Então os números de velocidade sobem por padrão, com o trabalho sendo bom ou não. Mais PRs, mais linhas, merges mais rápidos. Métricas de vaidade, todas elas, no momento em que o custo de produzir código cai para perto de zero.

Se você mede um time assistido por IA pela velocidade, você mede a única coisa que a IA infla de graça.

## Confiança é o número certo

[Frictionless](/pt-br/posts/2026-05-20-frictionless-the-book-behind-the-loop/) de Nicole Forsgren e Abi Noda nomeou a métrica que sobrevive à era da IA: Confiança, a dimensão que ele adiciona ao [framework SPACE](https://queue.acm.org/detail.cfm?id=3454124). A pergunta é simples. Você confia na saída o suficiente para colocá-la em produção sem refazer o trabalho?

Confiança é o número que não infla de graça. Um agente escreve dez PRs. Se você confia em duas o bastante para subir e reescreve as outras oito, sua velocidade foi teatro e sua saída real foi duas. Confiança é o que sobra depois que você subtrai o retrabalho.

Velocidade ainda importa. Ela está abaixo da Confiança agora. Um time que confia na saída da sua IA entrega rápido como efeito colateral. Um time que não confia entrega retrabalho com passos extras e um gráfico mais bonito.

## Revisão é uma disciplina, não um carimbo

Confiança é ganha ou perdida num único lugar: a revisão. O modelo é dono da execução, o desenvolvedor é dono da decisão. A revisão é onde o desenvolvedor toma a decisão. Três movimentos concretos separam uma revisão de verdade de um aceno de cabeça.

**Leia o diff, não o resumo.** O corpo do pull request do agente é uma hipótese do que ele fez. O diff é o que ele fez. A distância entre os dois é onde os bugs moram. Leia o diff.

**Rode.** Uma suíte de testes verde que o agente escreveu é necessária e não suficiente. O agente escreveu os testes e o código a partir do mesmo entendimento, então uma premissa ruim passa nos próprios testes alegremente. Rode a coisa. Veja o comportamento no caso que importa para você.

**Confira contra a spec.** A [spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) disse para que a mudança serve e para que ela não serve. A revisão confirma que a mudança faz aquilo, e só aquilo. Escopo que cresce a partir de um modelo afobado é o modo de falha silencioso. A spec é a régua contra a qual você mede.

Uma revisão de carimbo na saída de IA é o jeito mais rápido de perder Confiança sem perceber. Parece produtivo. Sobe as oito PRs que você deveria ter reescrito.

## Três métricas que dizem se o loop funciona

Você não precisa de trinta dashboards. Você precisa de três números nos quais age.

**Taxa de falha de mudança.** Das mudanças que você subiu, quantas precisaram de um conserto, um revert, ou um hotfix. Essa é a linha de base publicada da [DORA](https://dora.dev), e ela se lê diferente na era da IA. Uma taxa de falha de mudança subindo depois que você adota IA é um sinal direto de que o passo de revisão ficou fino demais. A saída parecia boa e não era.

**Taxa de retrabalho.** Com que frequência a saída de IA é jogada fora ou reescrita antes de subir. Esse é o número mais honesto específico da IA, porque ele é exatamente o inverso da Confiança. Retrabalho baixo significa que a spec estava clara e o modelo entregou. Retrabalho alto significa que a spec estava fraca ou o modelo está chutando, e seu gráfico de velocidade é ficção.

**Tempo-até-confiança.** Quanto tempo de "o agente propôs" até "um humano está confiante o bastante para subir". Esse é o cycle time real de um time assistido por IA. A parte do agente são segundos. A parte do humano é a revisão e a validação. Se o tempo-até-confiança não cai ao longo das semanas, o loop não está pagando, e mais agentes não vão consertar isso.

## O operador permanece no loop

[Salve o Tempo Chato](/pt-br/posts/2026-05-26-save-the-boring-time/) terminou numa regra: o agente faz triagem, rascunha, propõe, e nunca executa em produção sozinho. Um desenvolvedor que deu chaves de deploy a um agente por trinta dias colheu disso uma queda de 13 horas. A regra do operador-no-loop é o lado de segurança da Confiança.

Medir Confiança é como você sabe que o operador agrega valor e não só acena. Se a taxa de falha de mudança está estável, o retrabalho está baixo e o tempo-até-confiança está caindo, a revisão humana é trabalho real que paga. Se esses números derivam enquanto o humano segue aprovando, o loop tem um carimbo onde deveria ter uma revisão. As métricas dizem qual dos dois.

## O que isto não é

- Isto não é anti-métricas. Velocidade ainda conta. Ela fica abaixo da Confiança agora, não acima dela.
- Isto não é "meça tudo". Três números nos quais você age batem trinta que você ignora. Escolha os três, observe, mude algo quando eles se mexem.
- Isto não é uma auditoria de uma vez só. Confiança é uma medição contínua, do mesmo jeito que observabilidade era a fundação contínua da operação. Você observa, ou você perde.

## Fechamento

O loop foi feito para rodar rápido. Rápido nunca foi o ponto. Confiança era. O loop só vale a pena rodar se a saída é boa o bastante para subir sem refazer, e o único jeito de saber é medindo.

Velocidade te diz que o agente está ocupado. Confiança te diz que o trabalho valeu a pena. Meça a que sobrevive.
