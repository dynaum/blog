---
title: "Construindo um Jogo Só com IA: Como Lanterns Começou"
subtitle: "Um jardim aconchegante ao anoitecer, construído com a spec primeiro e o Claude como colaborador, mais a decisão que mudou tudo."
date: 2026-05-18
description: "Como Lanterns saiu de um pitch de uma frase para um jogo a caminho da Steam, por que troquei de engine no meio do projeto, e o que 'construído com IA' significa na prática."
---

Sou arquiteto de software durante o dia, em sistemas de saúde, o tipo de código onde "ir rápido" não é um elogio. À noite, faço jogos pequenos. **Lanterns** é o jogo que deixei uma IA construir comigo, de ponta a ponta, e este é o relato honesto de como ele começou: a ferramenta, a decisão de engine que quase saiu errada, e quanto disso o modelo está realmente fazendo.

## A ideia

Lanterns é um jardim aconchegante ao anoitecer. O jogo inteiro nasce de uma única virada cognitiva:

> Você aperta uma direção. O Guardião dá um passo para esse lado, e a lanterna balança para o lado *oposto*.

Essa assimetria é o jogo inteiro. Cada quebra-cabeça, cada onda da arena, é uma expressão de "pise numa verdade, ilumine outra". O pitch de onde parti era uma frase num documento de design:

> Um quebra-cabeça de jardim ao anoitecer: pise para um lado, a lanterna balança para o outro, capture vaga-lumes perdidos antes que a brisa os leve embora, e os guie para casa.

Nenhum código ainda. Só intenção. Isso importava, porque o primeiro artefato real não foi um protótipo, foi uma spec.

## A ferramenta: Claude Code, spec primeiro

Construí Lanterns com o [Claude Code](https://claude.com/claude-code), mas a parte que fez funcionar não é "a IA escreve código". É o **fluxo ao redor dela**: brainstorm → spec → plano → implementação, cada passo um documento commitado antes de uma linha de código de jogo existir.

O repositório ainda carrega todo o rastro em papel. Tem uma pasta `docs/superpowers/specs/` com documentos de design datados:

```
2026-04-23-lanterns-design.md
2026-04-24-arena-multiplayer-design.md
2026-04-25-steam-launch-polish-design.md
2026-04-29-hunt-pack-design.md
2026-04-29-mobile-friendly-web-design.md
2026-05-14-inventory-cap-design.md
...
```

Cada um é uma negociação de design de verdade: pitch, pilares, a mecânica enunciada com precisão, e os *não-objetivos* explícitos. A seção de não-objetivos é a coisa mais valiosa do processo, é onde "não seria legal se..." vai morrer antes de custar uma semana. O modelo é genuinamente bom na conversa de YAGNI quando você a torna parte do ritual em vez de um detalhe de última hora.

Só depois de uma spec aprovada é que um plano de implementação é escrito, e só então o código acontece. Como arquiteto, essa é a disciplina que eu quereria de qualquer engenheiro, e acontece que é também a disciplina que torna uma IA colaboradora confiável. O modelo não se perde quando o destino está escrito.

## A decisão que quase saiu errada: a engine

A primeira versão de Lanterns era **HTML + JavaScript + Canvas puro**. Sem framework, sem engine. É a escolha óbvia para um jogo de quebra-cabeça em grade: rápido de começar, roda em qualquer lugar, nada para instalar. Os primeiros commits constroem um núcleo de jogo limpo, um redutor puro em JS simples.

Aí bati na pergunta que todo projeto de jogo encontra: *esta é a engine na qual eu quero terminar, ou só a que foi fácil de começar?*

A spec deixou os pilares explícitos, e um deles era inegociável:

> **Os visuais são o produto.** A mecânica é o esqueleto; o brilho, o anoitecer e o detalhe colocado à mão são a *razão* de alguém jogar.

Um jogo aconchegante vive e morre pelo seu brilho, o jeito como a luz quente da lanterna floresce no anoitecer. No Canvas, esse brilho é matemática de shader feita à mão e muita composição frágil. A avaliação honesta, escrita no documento de design e depois num único commit decisivo:

> *Trocar a stack para Godot 4 pelo caminho nativo + Steam. Substitui a arquitetura HTML+JS+Canvas puro por Godot 4 / GDScript. Desktop nativo primário, demo web em HTML5 secundária. Ganhos principais: brilho via WorldEnvironment embutido (bloom), editor visual de TileMap, AnimationPlayer, autoria de níveis pelo editor, licença segura para uso comercial (MIT).*

O framework que eu usaria para *decidir* isso, e a parte que vale roubar, eram quatro perguntas:

1. **O que o produto está vendendo de fato?** Visuais. Então a renderização da engine tinha que ser uma força, não um projeto.
2. **Onde ele precisa ser publicado?** Desktop nativo e Steam, com uma demo web como funil, não o contrário.
3. **Qual é a exposição de licença?** Este é um lançamento comercial. A Godot é MIT. Isso remove uma categoria inteira de problema futuro.
4. **Qual é o custo de trocar *agora* contra depois?** O núcleo do jogo ainda era um pequeno redutor puro. Portá-lo era barato. Em seis meses não seria.

A pergunta 4 é a que as pessoas erram. Trocar de engine parece caro, então os times adiam até ficar de fato caro. Fazer a migração enquanto a base de código era pequena foi a decisão de maior alavancagem do projeto, e ter uma IA capaz de fazer o port mecânico rápido é exatamente o que tornou "trocar agora" a escolha racional em vez da assustadora.

## Quanto a IA está fazendo de fato?

Resposta honesta: muito, mas não a parte que as pessoas pensam.

Olhe o histórico do git e quase todo commit carrega um trailer `Co-Authored-By: Claude`. Cada spec de design foi escrita em diálogo com o modelo. Funcionalidades para as quais eu teria reservado uma semana, multiplayer local cooperativo, uma build com toque para celular, um sistema de limite de inventário com troca de slots, cada uma saiu em mais ou menos um dia a um dia e meio de trabalho focado, spec incluída.

Mas a alavancagem não é velocidade de digitação. É que o modelo é um colaborador incansável para o trabalho *chato mas decisivo*: escrever a seção de não-objetivos, fazer o port mecânico da engine, manter um arquivo de cena de 2.000 linhas sem apodrecer, extraindo subsistemas no prazo. O gosto, o que é aconchegante, o que é barato, quando uma mecânica é *divertida*, ainda tem que vir de um humano que jogou. A IA é extraordinária em execução e estrutura. Ela não é quem sabe que o brilho da lanterna está errado.

A divisão que funciona para mim: **eu sou dono da intenção e do julgamento; o modelo é dono da estrutura e da execução; a spec é o contrato entre nós.**

## Onde Lanterns está agora

É real. Dá para jogar no seu navegador agora mesmo em **[lanterns.dynaum.com](https://lanterns.dynaum.com)**, uma arena bullet-heaven aconchegante com cooperativo local, feita em Godot 4, a caminho da Steam. O modo quebra-cabeça que começou tudo ainda está lá, a uma flag de configuração de distância.

A coisa à qual eu sempre volto: nada disso funcionou porque a IA é mágica. Funcionou porque o processo, spec, não-objetivos, decidir cedo a coisa difícil, é o mesmo processo que torna times *humanos* bons, e o modelo é um participante genuinamente forte nele quando você segura essa linha.

Mais posts virão sobre as peças específicas: o design do cooperativo, o port para celular, e o próprio loop guiado por spec. Este é o post um.
