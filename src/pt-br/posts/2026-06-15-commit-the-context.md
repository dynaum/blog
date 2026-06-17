---
title: "Pague o Imposto de Setup Uma Vez"
subtitle: "O modelo esquece seu repositório a cada sessão, então alguém re-ensina os mesmos fatos para sempre. Um CLAUDE.md versionado e em camadas é como o repositório instrui o modelo para o time inteiro e para toda sessão que vier depois."
date: 2026-06-15
description: "Como acabar com o imposto de setup da IA usando CLAUDE.md: o arquivo que o modelo lê primeiro, suas quatro camadas (usuário, projeto, local, política), o carregamento por pasta em um monorepo, e por que commitá-lo transforma notas pessoais em infraestrutura de time."
cover: /assets/img/2026-06-15-commit-the-context.png
coverAlt: "Uma pilha de folhas translúcidas em camadas com texto Markdown tênue, cada uma brilhando mais quente em direção a uma única folha âmbar intensa na base, as camadas abrindo-se levemente em leque para ler como hierarquia, com luz de contorno ciano traçando as bordas das folhas."
---

Abra uma sessão nova em um repositório e a primeira coisa que você faz é ensinar. "Este projeto usa pnpm, não npm. Os testes ficam em `test`, não ao lado do código. Não edite nada dentro de `generated`." Você já digitou essas frases antes. Vai digitar de novo amanhã. E o desenvolvedor ao seu lado também.

O modelo esquece cada repositório entre sessões. [A janela de contexto é uma mesa, não uma memória](/pt-br/posts/2026-06-10-context-window-desk-not-memory/): cada sessão começa limpa, e os fatos permanentes sobre seu código vão embora quando a aba fecha. O ensino não é opcional e ninguém está sendo preguiçoso. É estrutural. Alguém re-paga isso a cada sessão, para sempre, a menos que o próprio repositório carregue a lição.

O repositório carrega no lugar. A solução é um arquivo versionado.

## O arquivo que o modelo lê primeiro

`CLAUDE.md` é um arquivo Markdown no seu repositório que o modelo lê automaticamente no início de toda sessão. Sem comando, sem colar. Você escreve os fatos permanentes do projeto nele uma vez: os comandos de build e de teste, as convenções, os diretórios em que não se mexe, a pegadinha que te mordeu mês passado. Faça o commit. A partir daí, toda sessão de todo desenvolvedor abre com esse contexto já em cima da mesa.

Essa é a jogada inteira. O imposto de setup cai de uma-vez-por-desenvolvedor-por-sessão para uma vez, no total. Os vinte minutos de colocar o modelo a par viram um arquivo que você escreveu em março.

## Quatro camadas, a mais próxima vence

O arquivo não é um arquivo. É uma pilha.

- **Sua camada.** `~/.claude/CLAUDE.md` guarda suas preferências em todos os projetos que você abre: seu estilo, seus hábitos, o jeito que você gosta que os commits sejam escritos. Ela viaja para dentro de todo repositório e fica de fora de todos eles.
- **A camada do projeto.** `./CLAUDE.md` na raiz do repositório guarda os fatos do time. Esta é a que você commita.
- **A camada local.** `CLAUDE.local.md`, no gitignore, guarda o que é verdade só na sua máquina: uma URL de sandbox, um caminho local, um atalho pessoal. Sua, nunca enviada.
- **A camada de política.** Organizações definem um arquivo gerenciado que todo repositório herda, para as regras que não estão em discussão.

O modelo concatena todas elas, e a camada mais próxima do seu trabalho carrega por último, então o específico vence o geral. A divisão que paga o próprio custo são as duas do meio. Os fatos do time vão no arquivo versionado. Os fatos pessoais e de máquina vão no arquivo no gitignore. Commite o que todos precisam, deixe de fora o que só você precisa, e o repositório nunca carrega o caminho local de outra pessoa.

## Contexto que segue a pasta

Um `CLAUDE.md` na raiz não precisa guardar tudo. Coloque um `CLAUDE.md` dentro de uma subpasta e o modelo o carrega apenas quando trabalha em arquivos daquela subárvore.

É isso que faz a coisa escalar. Um monorepo com um serviço em Go, um app React e um schema compartilhado ganha três arquivos de contexto pequenos, cada um ao lado do código que descreve. O modelo trabalhando no app React nunca carrega as regras do serviço em Go. Cada pasta instrui o modelo sobre si mesma, sob demanda, e nenhuma sessão arrasta a árvore inteira junto.

## Entre projetos, não só entre pessoas

O imposto de setup não é só um custo de time. Você o paga entre seus próprios projetos também. Todo repositório novo que você abre é outra mesa limpa.

A camada de usuário é a solução entre projetos. As preferências que você coloca em `~/.claude/CLAUDE.md` te seguem para dentro de todo projeto, então o jeito que você trabalha fica definido uma vez para todos eles. Para o conhecimento durável que sobrevive a qualquer repositório, as regras de domínio e as lições suadas, [um vault compartilhado](/pt-br/posts/2026-05-22-your-ai-context-belongs-to-the-team/) é o lar, e o arquivo do projeto aponta para os detalhes. O vault guarda o que continua verdade entre projetos. O arquivo versionado guarda o que é verdade para este aqui.

## Commite, ou pague o imposto para sempre

Aqui está a frase que importa. Um arquivo de contexto não versionado é uma nota pessoal. Um versionado é infraestrutura.

Uma nota ajuda você, na sua máquina, até você formatar o notebook. Infraestrutura ajuda todo mundo, em toda máquina, em toda sessão, e versiona junto com o código, então continua verdadeira conforme o código muda. No instante em que você commita o `CLAUDE.md`, o imposto de setup é pago uma vez para o time inteiro e para toda sessão que vier depois. Quando você se pega explicando a mesma coisa duas vezes, esse é o bug, e a solução é um parágrafo em um arquivo que você já tem.

Uma observação sobre nomes. `CLAUDE.md` é o nome de arquivo do Claude Code. `AGENTS.md` é a mesma ideia que outras ferramentas leem. Mesma jogada, rótulo diferente.

## O repositório lembra por você

O modelo começa toda sessão do zero. E vai começar, toda vez, por design. `CLAUDE.md` é como o repositório lembra no lugar dele. Escreva os fatos permanentes, faça o commit, e o próximo desenvolvedor a abrir uma sessão, incluindo a versão futura de você, começa já instruído. Pague o imposto uma vez.
