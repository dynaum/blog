---
title: "Construa Suas Próprias Ferramentas"
subtitle: "Uma ferramenta que custava uma sprint agora custa uma tarde. A decisão sobre o que construir é o gargalo. Um desafio direto: escolha uma tarefa que você fez duas vezes esta semana e tenha uma ferramenta sob medida para ela até amanhã à noite."
date: 2026-05-28
description: "A curva de custo para construir ferramentas internas customizadas virou: de sprint para tarde. O gargalo agora é a decisão sobre o que construir, não a construção em si. Três categorias de ferramentas que você pode construir hoje (CLIs, ferramentas web pequenas, extensões de quick-launcher), e um desafio de 24 horas para agir."
cover: /assets/img/2026-05-28-build-your-own-tools.png
coverAlt: "Uma oficina escura de artesão à noite. Várias ferramentas pequenas feitas à mão estão sobre uma bancada de madeira pesada, cada uma com formato ligeiramente diferente. Uma lanterna âmbar quente no centro é a fonte de luz dominante."
---

Tenho construído pequenas ferramentas para mim mesmo há anos. O blog que você está lendo roda num setup customizado de Eleventy. Minhas notas vivem numa estrutura customizada de vault no Obsidian. Os jogos que faço à noite vêm com seus próprios scripts internos. Construir ferramentas sob medida não é novidade.

A diferença agora é que uma tarde é o bastante.

Uma ferramenta que custava uma sprint custa uma tarde, porque o modelo escreve o código enquanto o desenvolvedor decide para o que o código serve. O custo de um experimento caiu para um bom prompt e uma sessão de review. A maioria dos devs com quem trabalho ainda não internalizou isso. Eles continuam abrindo o ticket e torcendo para alguém construir. A curva de custo virou debaixo desse hábito, e o hábito não percebeu.

O gargalo se moveu. Não é mais "eu consigo construir isso?". É "eu deveria?". A resposta é simples: qualquer coisa que você faz mais de duas vezes neste mês é candidata.

A maioria dos devs que conheço está em cima de cinco dessas candidatas hoje e não as vê, porque a matemática antiga (uma ferramenta custa uma sprint, meu tempo é da empresa, ninguém aprova) ainda está rodando no fundo. Rode a matemática nova: a ferramenta custa uma tarde, o payoff é toda semana pelo resto do projeto. A decisão fecha já na primeira vez.

As candidatas se escondem à vista. O resumo de standup matinal que você escreve à mão. A triagem de pull-requests que você faz toda segunda. O fetch-e-formata dados que você faz toda vez que alguém pede um status. A caça de "onde caiu aquele bug" entre três repositórios. A tradução repetida entre o vocabulário da sua ferramenta e o do sistema implantado. Todas parecem pequenas porque cada uma é pequena. O tamanho que importa é o ano que você continua pagando por elas.

## Três categorias

**CLIs internas.**

Um script em `bin/` que pega a coisa chata e repetitiva e transforma em um comando. Exemplo: `bin/standup` lê o git log de ontem, chama um modelo para resumir o que subiu (mensagens de commit não mentem, mas leem como ruído), e escreve o resumo na nota do dia no seu vault. Construído numa noite com [Bun](https://bun.sh) e uma única chamada ao Anthropic SDK. O agente faz o resumo-a-partir-do-diff. A CLI te dá `bin/standup` como verbo. Diário, roda em cinco segundos, saída pronta quando você abre o notebook.

**Ferramentas web pequenas.**

Um app de uma página que vive em `localhost:3000` e substitui um fluxo que você faz hoje em cinco abas. Exemplo: um board de triagem que lê sua caixa de entrada e as issues do repositório, pede para um modelo ranquear por urgência e agrupar por tema, e te deixa arrastar as cinco do topo para "hoje" enquanto o resto vai para "semana que vem". [Bun](https://bun.sh) mais [Hono](https://hono.dev) no backend, Vite mais Tailwind no frontend, tudo rodando na sua máquina. Uma tarde, não uma sprint. O [Tauri](https://tauri.app) embrulha como app de desktop se você quiser um sem aba de navegador.

**Extensões de quick-launcher ou bots.**

Uma extensão do [Raycast](https://developers.raycast.com) no macOS ou um pequeno bot no Slack ou Discord que transforma "troca de contexto, roda um comando, volta" em um único atalho ou uma única mensagem. Exemplo: um comando do Raycast que pega um parágrafo selecionado e reescreve na voz do blog, com as regras de estilo certas já anexadas ao prompt. Duas horas, incluindo a parte em que eu argumentei com o modelo se "just" era uma palavra banida. Agora ele entrega com as regras embutidas.

O padrão se repete nas três. A ferramenta te dá a superfície certa: um verbo de CLI, uma UI em localhost, um atalho, uma mensagem no Slack. O agente faz o coletar-e-correlacionar dentro da ferramenta. Você continua sendo quem decide. Mesma divisão de trabalho de todo outro post. Escopo menor, loop mais rápido.

## O que isto não é

Seção honesta, três bullets.

- Isto não é "a IA constrói a ferramenta enquanto você senta". Você ainda escreve a spec da ferramenta, decide para o que ela serve, e revisa o código. Mesma divisão de trabalho de todo outro post.
- Isto não é substituto para as ferramentas do time de plataforma. Use aquelas quando existem. Construa as suas quando o atrito é seu e o time de plataforma está a seis meses de distância.
- Isto não é um pitch de vibe-coding. O mesmo [loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) se aplica: brainstorm, spec, plano, implementação. A ferramenta que levou uma tarde para construir é a ferramenta que sobrevive porque você fez a spec.

## O desafio

Escolha uma tarefa que você fez pelo menos duas vezes esta semana. Escreva num post-it. O resumo de standup matinal. A triagem de pull-requests. O relatório recorrente. A tradução de ticket-do-Jira-para-PR. A caça de "onde caiu aquele bug" entre repositórios. A que você lembra sem precisar pensar.

Agora pergunte uma coisa: se uma ferramenta sob medida rodasse essa tarefa para mim, o resultado chegaria em menos de um minuto e me deixaria seguir em frente?

Se sim, a resposta para "eu deveria construir?" é sim. O custo é uma tarde. O payoff é toda semana enquanto você continua trabalhando nessa base de código.

Vinte e quatro horas. Até amanhã à noite você construiu ou decidiu que não vale a pena. Qualquer das duas respostas serve. A que este post está desafiando é o default de "eu chego nela depois".

## Fechando

O blog passou dez posts sobre IA como colaboradora no trabalho que você já faz. Este post é o que diz: o trabalho que você faz não é fixo. O conjunto de ferramentas a que você tem acesso não é fixo. Construa as que combinam com o trabalho que você realmente faz, não as que um produto genérico atende.

Ferramentas que você constrói são o atrito que você deixa de pagar.
