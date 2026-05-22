---
title: "O Loop Guiado por Spec: Como Eu Realmente Trabalho com uma IA"
subtitle: "Brainstorm, spec, plano, implementação. Cada um um documento commitado antes de uma linha de código. A seção de não-objetivos é a coisa de maior alavancagem que escrevo na semana."
date: 2026-05-19
description: "O método repetível por trás de Lanterns, generalizado: por que uma spec escrita com não-objetivos explícitos torna uma IA colaboradora confiável, com artefatos reais do repositório."
cover: /assets/img/2026-05-19-the-spec-driven-loop.png
coverAlt: "Uma única lanterna quente brilhando numa mesa escura de arquiteto à noite, papéis empilhados pegando a luz, código tênue numa tela através da janela."
---

[O post um](/pt-br/posts/2026-05-18-building-lanterns-with-ai/) contou a história de como Lanterns começou. Ele terminou com uma promessa: mais posts sobre as peças específicas, começando pelo loop em si. Este é esse post.

O loop não é específico de jogos. Uso os mesmos quatro passos para o trabalho de backend em saúde no meu emprego e para um jogo aconchegante à noite. O meio muda. A disciplina não.

## O loop

Quatro passos. Cada um produz um documento commitado antes do próximo começar:

```
brainstorm  →  spec  →  plano  →  implementação
 (conversa)    (.md)    (.md)    (código + commits)
```

A ordem é o ponto inteiro. Nenhuma spec até o brainstorm assentar. Nenhum plano até a spec ser aprovada. Nenhum código até o plano existir. O modelo é rápido o bastante para pular direto para o código, e pular é o erro mais caro que você comete com ele.

Você vê o loop no histórico do git, não só na minha descrição dele. A funcionalidade de limite de inventário entrou nesta sequência:

```
a35ddd4  docs: spec for inventory cap with slot-based swap
6bb80be  docs: implementation plan for inventory cap with slot-based swap
de63871  feat(arena): Inventory data model with 6-slot cap and ever-held tracking
c386d03  refactor(arena): route picks through Inventory; stub apply path
...
24f8fac  Merge feat/inventory-cap: 6-slot capped, swap-based upgrade inventory
```

Commit da spec. Depois commit do plano. Depois treze commits de funcionalidade. Os documentos são datados e versionados ao lado do código que produziram. Daqui a um ano, eu leio a spec para lembrar do porquê, não o diff para adivinhar.

## Passo 1: brainstorm

Este passo é conversa, não arquivos. Eu descrevo a intenção. O modelo rebate, propõe alternativas, nomeia riscos. O objetivo é um parágrafo com o qual nós dois concordamos.

A spec do limite de inventário registra onde isso chegou, incluindo um caminho rejeitado:

> Affordances específicas de slot (slots de habilidade ativa separados dos passivos, essa foi a opção C no brainstorm e foi rejeitada).

Escrever a opção rejeitada importa. Seis semanas depois, quando alguém pergunta "por que não separar os slots ativos?", a resposta está no repositório. O brainstorm é barato. Relitigar uma decisão já fechada não é.

## Passo 2: a spec, e seus não-objetivos

A spec enuncia o pitch, os pilares, a mecânica com precisão, e os não-objetivos. A seção de não-objetivos é a coisa mais valiosa que escrevo na semana.

Aqui está uma real, na íntegra, do design do cooperativo local:

> **Escopo excluído de propósito do v1**
> - 3+ jogadores
> - Tela dividida
> - Multiplayer em rede (só local, mesma tela)
> - Fogo amigo entre os feixes dos jogadores
> - Trocar upgrades entre jogadores
> - HP compartilhado / modo caído-é-morto
> - Modos competitivos
>
> Todas são versões futuras razoáveis, mas cada uma dobra a complexidade. O primeiro v1 deve ser: dois amigos, um sofá, aconchegante.

E da spec do limite de inventário:

> **Fora de escopo (explícito)**
> - Rearranjo de slots com arrastar e soltar.
> - Um botão de "pular esta escolha" quando cheio. Será adicionado depois se os playtests mostrarem que trocas forçadas parecem punitivas.
> - Tooltips ao passar o mouse ou segurar na tira durante a luta.
> - Rebalancear famílias de upgrade ou novos upgrades. O limite é uma mudança estrutural, não de conteúdo.

Cada linha dessas listas é uma ideia boa o bastante para ser tentadora. Cada uma também é uma semana de trabalho e uma nova categoria de bug. A seção de não-objetivos é onde "não seria legal se" vai morrer antes de custar qualquer coisa.

Esta é a parte em que o modelo é inesperadamente bom. Peça a uma IA para adicionar uma funcionalidade e ela vai adicionar a funcionalidade, mais três que você não pediu. Torne os não-objetivos uma seção obrigatória de toda spec e a conversa se inverte. Agora o modelo argumenta *a favor* de cortar escopo, porque o documento exige uma razão para tudo que fica. A disciplina vive no ritual, não em lembrar de ser disciplinado.

## Passo 3: o plano, e o registro de decisões

Uma vez que a spec é aprovada, o plano a transforma em passos ordenados. Ele também carrega um registro de decisões: cada escolha não óbvia, com a razão anexada. Do trabalho do limite de inventário:

> - **Tamanho do limite: 6.** Alinha com as convenções de Vampire Survivors / Brotato, combina com a duração média de uma run para que a mecânica de troca de fato dispare.
> - **Contagem de slot por escolha (sem fusão automática de duplicatas).** Cada escolha custa um slot, inclusive as idênticas. Honesto sobre o custo de empilhar.
> - **Reversão de efeito via reset + reaplicação.** Uma única fonte da verdade dirige cada atributo. Sem lógica de reversão por upgrade.

Uma decisão sem a razão apodrece. Seis meses depois você não consegue distinguir uma restrição deliberada de um acidente, então tem medo de tocar em qualquer uma das duas. A razão é o que torna o código seguro de mudar mais tarde.

## Passo 4: implementação

Só agora o código acontece, e este é o passo que as pessoas supõem ser o trabalho inteiro. É o menos interessante. Com a spec e o plano escritos, a implementação é execução contra um contrato. O modelo é excelente nisso: incansável, estruturalmente consistente, feliz em extrair um arquivo de cena de 2.000 linhas em subsistemas no prazo em vez de deixá-lo apodrecer.

A alavancagem nunca foi velocidade de digitação. É que os passos um a três removeram toda ambiguidade antes da primeira linha de código, então o modelo nunca teve que adivinhar o que eu quis dizer. Um modelo que não adivinha não se perde.

## Por que isso generaliza

Nada acima é sobre jogos. Troque "brilho da lanterna" por "análise de sinistros" e o loop é idêntico. A razão de funcionar é a razão de funcionar para times humanos: uma spec escrita com não-objetivos explícitos é o lugar mais barato para errar. Errar num parágrafo custa um parágrafo. Errar numa funcionalidade já integrada custa uma sprint.

A divisão do post um continua valendo, e o loop é o que a faz valer:

> Eu sou dono da intenção e do julgamento. O modelo é dono da estrutura e da execução. A spec é o contrato entre nós.

O contrato é a palavra que sustenta tudo. Sem ele, "assistido por IA" significa um estagiário rápido sem briefing. Com ele, o modelo é o participante mais forte de um processo que já tornava bons times bons.

A seguir nesta série: o design do cooperativo local e o port para a web mobile. Os dois rodaram exatamente este loop. Os dois têm os comprovantes no repositório.
