---
title: "Agentes São Sistemas, Não Prompts"
subtitle: "Todo mundo pergunta LangChain ou CrewAI primeiro. Pergunta errada. Um agente de produção é arquitetura: uma política de memória, um orçamento de contexto, uma decisão de modelo, e um prompt com guardrails. O framework é a parte fácil."
date: 2026-06-03
description: "Construir um agente que roda no seu próprio sistema é engenharia de sistemas, não escrita de prompt. As quatro decisões que definem se ele funciona (problema, memória, contexto, escolha de modelo) e o prompt de sistema em três partes: comportamento, guardrails, limites."
cover: /assets/img/2026-06-03-agents-are-systems-not-prompts.png
coverAlt: "Um corte transversal de um motor sobre uma bancada escura, vários componentes distintos conectados e ligados entre si, brilhando em âmbar quente por dentro, com luz de contorno azul-petróleo nas carcaças de metal."
---

A primeira pergunta que as pessoas fazem quando querem construir um agente é "LangChain ou CrewAI?". É a pergunta errada para começar. O framework é a menor decisão que você vai tomar, e você a toma primeiro porque é a única parte que parece uma escolha.

Um agente de produção não é um prompt esperto rodando num loop. É um sistema. Tem uma política de memória, um orçamento de contexto, uma decisão sobre qual modelo cuida de qual passo, e um prompt que funciona como um contrato. Essas são decisões de arquitetura, e elas definem se o agente funciona muito antes do framework. Construa um agente do jeito que você constrói qualquer sistema, porque é isso que ele é.

## O framework é a parte fácil

Escolha os seus dois. O LangChain, através do LangGraph, te dá componentes mais um grafo para agentes com estado, de longa duração, de múltiplos passos. O CrewAI te dá agentes baseados em papéis trabalhando como uma equipe, e hoje ele se sustenta sozinho, sem LangChain por baixo. Os dois são Python. Os dois são mantidos. Os dois convergem para a mesma forma.

Escolha aquele cujo modelo encaixa em como você pensa o seu problema, e siga em frente. A escolha é real, mas é pequena, e é reversível. Você troca o framework numa semana. Você não troca um modelo de memória que nunca desenhou. Gaste seu pensamento onde ele não volta barato.

## As quatro decisões

**Entenda o problema.** Um sistema autônomo amplia uma spec vaga. Um humano preenche uma lacuna no briefing com julgamento. Um agente preenche com o que está estatisticamente por perto, e age sobre isso, em escala, sem parar para perguntar. Antes de qualquer código, escreva para o que o agente serve, como é estar pronto, e onde acaba a autoridade dele. Um problema difuso produz um agente que vagueia, toda vez. Esta é a decisão que sustenta tudo e a que as pessoas pulam para chegar na parte divertida.

**Controle a memória.** Um agente sem política de memória ou esquece tudo entre os passos ou lembra de tudo até o contexto afogar. Nenhum dos dois funciona. Decida de propósito. O que persiste entre execuções. O que vive só dentro de uma execução. O que é resumido em uma frase. O que é jogado fora no instante em que o passo termina. Memória é uma decisão de design com um custo, não um botão que você liga. Diga o que o agente guarda, e diga por quê.

**Gerencie o contexto.** Contexto é um orçamento, não um balde. Cada token gasto em histórico velho é um token não gasto na tarefa diante do modelo, e uma janela inchada faz o modelo derivar do mesmo jeito que um prompt arrastado faz. Decida o que entra na janela em cada passo, em que ordem, e o que é despejado para abrir espaço. A habilidade é alimentar o modelo exatamente com o que este passo precisa e nada mais. A maioria dos agentes que "ficam mais burros com o tempo" não está ficando mais burra. O contexto deles está enchendo de ruído.

**Encaixe o modelo na tarefa.** Um modelo para todo passo é desperdício de um lado e fraqueza do outro. Use um modelo barato e rápido para classificação e roteamento. Use um forte para o passo de raciocínio difícil que de fato precisa. Use o menor modelo que passa da régua para todo o resto. Esta é uma decisão que você toma por passo, não uma vez para o agente inteiro. Pagar pelo modelo de ponta para analisar um sim-ou-não é como um agente fica caro sem ficar melhor.

## O prompt: comportamento, guardrails, limites

O prompt de sistema não é um desejo que você sussurra para o modelo. É um contrato, e um contrato tem partes.

**Comportamento.** O papel e como ele age. O que faz, em que ordem, em que voz, com quais padrões. Específico o bastante para o agente não inventar a própria descrição de cargo a partir das lacunas que você deixou.

**Guardrails.** Os "nunca" absolutos. O que ele não pode fazer sob nenhuma entrada, incluindo as entradas que você não imaginou. Trabalho num domínio regulado onde código errado tem consequências, e é aqui que moram as restrições inegociáveis, escritas como absolutos, não como preferências que o modelo pode pesar contra ser prestativo.

**Limites.** Escopo e condições de parada. O que está fora dos limites, e quando parar e devolver para um humano em vez de seguir empurrando. Um agente sem condição de parada não sabe quando terminou, então nunca termina. Ele entra em loop, ou alarga o próprio escopo até quebrar algo.

Um prompt com as três é um contrato que o agente consegue cumprir. Um prompt faltando uma é a fresta por onde a falha entra.

## O que isto não é

- Não é uma guerra de frameworks. LangChain e CrewAI funcionam. O post não é sobre qual vence, porque não é essa a decisão que importa.
- Não é sobre ferramentas ou dar mãos ao agente. Esse é o próximo post, de propósito. Aqui o agente raciocina e decide. Deixá-lo agir sobre o mundo é um tema próprio, com seus próprios modos de falha.
- Não é uma afirmação de que prompts não importam. Importam enormemente, e é exatamente por isso que o prompt ganha uma estrutura em vez de um chute.

## Fechamento

O framework é por onde todo mundo começa porque é a parte que parece construção. A construção de verdade é mais acima, nas decisões que não têm logo: para o que o agente serve, o que ele lembra, o que ele vê, qual modelo usa, e o contrato sob o qual roda.

Acerte essas e qualquer framework vai carregá-las. Erre essas e nenhum framework vai te salvar. O agente é um sistema. O prompt é um contrato. O framework é só a sala onde eles moram.
