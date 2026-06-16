---
title: "Stratify: O Tamanho do Que Uma Pessoa Entrega Hoje"
subtitle: "Um motor de análise estática poliglota. Cinco linguagens e seis análises sobre um único modelo, chegando ao seu terminal, CI, editor, agente de IA e dashboards. Construí sozinho, com o loop guiado por spec. A manchete não é a ferramenta. É o quão pouco custou."
date: 2026-06-14
description: "Apresentando o Stratify, um motor de análise estática poliglota e open source: cinco linguagens, seis análises, um IR universal e cinco superfícies. Construído sozinho com o loop guiado por spec, e por que uma arquitetura limpa é o que deixa uma pessoa entregar uma plataforma completa."
cover: /assets/img/2026-06-14-stratify-launch.png
coverAlt: "Cinco estratos minerais distintos em tons frios comprimindo-se para baixo em um único núcleo âmbar incandescente, que se abre de volta em feixes de luz brilhantes, com luz de contorno ciano traçando as bordas dos estratos."
---

Cinco linguagens. Seis análises. Cinco superfícies. Um binário. Uma pessoa.

Essa última linha é a manchete. O Stratify lê um repositório inteiro escrito em Java, Ruby, TypeScript, Python ou Go, constrói um único modelo dele e roda seis análises estáticas sobre esse modelo. Os resultados chegam até você em cinco lugares: seu terminal, um gate de CI, seu editor, seu agente de IA e um dashboard de frota. Construí sozinho. Um ano atrás, a última frase seria mentira, ou uma rodada de investimento.

Hoje o Stratify é público.

## O que ele faz

Aponte para um repositório e rode um comando.

```
stratify check .
```

```
warn  Unused.java:2  unused function `neverCalled`
info  App.java:6  possibly unused function `helper`

2 finding(s).
```

Seis análises rodam em uma única passagem: código morto, duplicação, complexidade, hotspots de churn, ciclos de dependência e fronteiras de camada que quebram as regras da sua arquitetura. Cada achado carrega um nível de confiança. Quando o Stratify não consegue provar que uma função está morta, ele diz `possibly unused` em vez de `unused`. Ele nunca marca código funcionando como morto porque a resolução ficou difícil.

O mesmo motor se abre em cinco superfícies. A CLI imprime achados ou emite JSON e SARIF para code scanning. Uma GitHub Action transforma qualquer varredura em um gate de qualidade. Um servidor MCP deixa seu agente de código consultar os achados direto, em vez de fazer parsing do texto do terminal. Um language server entrega os mesmos diagnósticos dentro do seu editor. Um exportador OpenTelemetry empurra cada execução para um dashboard, então você acompanha a saúde do código ao longo do tempo em uma frota de repositórios. Uma análise, cinco lugares onde você já trabalha.

Essa amplitude é a história de uso. A parte que acho mais interessante vem agora.

## A decisão única que barateou tudo

Cinco linguagens parecem cinco vezes o trabalho. Não foram, por causa de uma única decisão tomada cedo.

Toda análise lê um único modelo compartilhado, nunca o código-fonte. O tree-sitter faz o parsing de cada linguagem para um IR Universal: símbolos e referências, cada um marcado com um nível de confiança. As seis análises leem apenas esse IR. Elas nunca veem Java, Go ou Ruby. Elas veem a mesma forma toda vez.

Então adicionar uma linguagem é um único adaptador que emite o IR. As seis análises vêm junto, intocadas. Foi assim que o Stratify foi de uma linguagem para cinco sem mudar uma linha de código de análise. O escopo cresceu. O trabalho não cresceu junto.

## Por que a mesma arquitetura sustentou o loop

Aqui está a parte que este blog não para de rodear.

O loop que descrevo, brainstorm, spec, plano, implementação, não se sustenta porque o modelo é mágica. Ele se sustenta porque a arquitetura mantém cada peça pequena. Cada análise é uma unidade com um trabalho, uma entrada, o IR, e uma saída testável, os achados. Eu seguro uma única análise na cabeça. O modelo também. A spec dela cabe em uma página. O teste dela é um repositório de exemplo e um relatório esperado.

Boas fronteiras são por que um time humano estende um código barato. As mesmas fronteiras são por que o [loop o constrói de forma confiável](/pt-br/posts/2026-06-03-agents-are-systems-not-prompts/). É a mesma propriedade. Um código fatiado em unidades pequenas e bem delimitadas é fácil de uma pessoa raciocinar e fácil de um modelo construir, pela mesma razão: você segura só uma peça por vez.

A arquitetura é a coisa que uma pessoa decide. O modelo não escolheu o IR. [Eu escolhi](/pt-br/posts/2026-05-19-the-spec-driven-loop/). Essa escolha é o que deixou tudo depois dela tratável.

## O que "completo" significa aqui

Uma demo é fácil. Completo é a parte chata.

Completo significa um binário que você instala com Homebrew ou uma linha de curl. Uma GitHub Marketplace Action versionada que baixa um binário pré-compilado e sobe em segundos. SARIF 2.1.0 que o GitHub renderiza como anotações inline em um pull request. Um servidor MCP e um language server de editor. Exportação OTLP com labels de métrica limpas. Um teste ponta a ponta para cada linguagem em cada superfície, porque cinco linguagens vezes seis análises vezes cinco superfícies é onde os bugs reais se escondem.

Esse último quilômetro é a maior parte do trabalho em qualquer produto real. [Construa Suas Próprias Ferramentas](/pt-br/posts/2026-05-28-build-your-own-tools/) defendeu que uma ferramenta sob medida hoje custa uma tarde. Lancei o [Conduit](/pt-br/posts/2026-06-12-conduit-launch/) do mesmo jeito alguns dias atrás. O Stratify é essa curva levada a uma plataforma. A tarde virou algumas semanas. O time continuou em um.

## A parte honesta

O time era eu e o modelo, a mesma divisão de trabalho que todo post aqui descreve. Eu fui dono da intenção e das decisões que sustentam tudo. O IR. A escolha de reportar `possibly unused` em vez de chutar, porque um analisador estático que grita lobo é desligado em uma semana. O modelo foi dono da estrutura e da execução: os adaptadores, as análises, a fiação das superfícies, os testes.

Eu guiei mais onde a correção era sutil. A resolução de chamadas entre arquivos quer exagerar nos relatos de código morto no instante em que perde uma referência. Ensiná-la a dizer "não tenho certeza" em vez de "isto está morto" exigiu julgamento, não geração. Esse julgamento é o trabalho que continuou meu.

## O que isto não é

- Não está pronto. É a v0.1: cinco linguagens e um contrato de IR construído para que a cauda longa de linguagens seja um adaptador cada.
- Não é um substituto das ferramentas nativas da sua linguagem. É o único relatório que abrange todas elas.
- Não é prova de que o modelo trabalha sozinho. É prova de que uma pessoa, o loop e uma arquitetura limpa entregam o que um time costumava entregar.
- Não está à venda. O Stratify é open source, ponto final.

## Experimente

Clone o [repositório](https://github.com/stratify-dev/stratify), instale o binário e rode `stratify check .` no seu repositório poliglota mais bagunçado. Leia os níveis de confiança, não só os achados. Os warnings são onde ele tem certeza. O resto é onde ele te diz que está chutando, que é a parte que a maioria das ferramentas nunca admite.
