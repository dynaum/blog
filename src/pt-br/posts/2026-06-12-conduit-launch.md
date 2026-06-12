---
title: "Conduit: O Encanamento Que Todo Time de RAG Reconstrói"
subtitle: "Uma aplicação de RAG é 20 por cento lógica de retrieval e 80 por cento encanamento de dados, e todo time reconstrói os mesmos 80 por cento do zero. Eu construí um motor open source que cuida disso. Hoje ele é público."
date: 2026-06-12
description: "Anunciando o Conduit, o motor open-core de frescor de dados para RAG. Conectores, chunking, embedding, sync incremental e monitoramento de frescor em um motor que escreve no seu vector store em vez de ser dono dele. Construído solo com o loop guiado por spec."
cover: /assets/img/2026-06-12-conduit-launch.png
coverAlt: "Uma rede de canos industriais escuros convergindo para um único conduíte brilhando em âmbar quente, alimentando um recipiente de luz, com luz de contorno azul-petróleo traçando as juntas dos canos."
---

Ninguém começa querendo construir um pipeline. Você começa querendo construir a feature: um bot de suporte que conhece a documentação, uma busca que entende a codebase, um assistente que responde a partir do seu conhecimento em vez de chutar. Então você descobre a proporção. Retrieval, a parte que você queria construir, é uns 20 por cento do trabalho. Os outros 80 por cento são encanamento, e todo time reconstrói o mesmo encanamento do zero.

Eu cansei da proporção. Então construí o Conduit, e hoje ele é público.

## Os 80 por cento

[Conhecimento estável mas grande demais para todo prompt](/pt-br/posts/2026-06-11-prompt-vs-tool/) mora no retrieval. Levar esse conhecimento até lá, e mantê-lo verdadeiro, é uma lista de tarefas que todo time repete.

Primeiro vêm os conectores. Seu conhecimento mora em pastas, sites, bancos de dados, buckets e repositórios, e cada fonte tem sua própria API, sua própria autenticação e seu próprio jeito de mudar. Depois o chunking, dividir documentos em pedaços que valem a pena recuperar, que depende do tipo de documento e é fácil de errar de um jeito sutil. Depois o pipeline de embedding, que parece uma linha de código na demo e vira engenharia de verdade no dia em que chegam o volume e as falhas. Depois o sync incremental, porque documentos mudam, e a versão atualizada precisa chegar ao vector store sem reprocessar o mundo.

Depois o frescor, a tarefa que ninguém assume. É nela que mora a falha silenciosa. Nada avisa que uma fonte ficou inacessível ou que um documento envelheceu. O índice não reclama. O modelo lê chunks velhos do jeito que lê tudo, como verdade absoluta, e responde com total confiança. O primeiro sinal de que seu pipeline quebrou é um usuário recebendo uma resposta errada, educadamente.

Todo time escreve essa pilha uma vez, mal, com prazo apertado. E mantém para sempre.

## O que é o Conduit

O [Conduit](https://github.com/dynaum/conduit) é um motor que cuida desses 80 por cento. Você aponta para as suas fontes, arquivos, sites, Postgres, S3, GitHub, e para o seu vector store. Ele ingere, parseia, divide, gera embeddings e mantém tudo em sync.

A palavra que sustenta o peso é sync. Rode duas vezes e a segunda execução pula tudo. Edite um documento e só ele gera embeddings de novo. Apague um e os vetores dele desaparecem na próxima execução. Um documento que falhou fica registrado e é tentado de novo depois, enquanto o resto da execução termina. O chunking entende estrutura: Markdown divide por heading, PDF por página, código nos limites de alto nível, e cada chunk carrega seu caminho de headings, número de página ou linguagem como metadado que você consulta.

Duas coisas que o Conduit se recusa a possuir, de propósito. Ele não é dono do seu vector store: os embeddings caem na sua tabela Postgres, e você os lê com SQL puro, do jeito que sua aplicação preferir. E ele não é dono da sua lógica de retrieval: ranking, filtros e o que você faz com os chunks continuam seus. O Conduit é a camada de extract-and-load por baixo, nada mais.

Uma linha honesta sobre o modelo. O motor é open source sob MIT, e a parte que eu pretendo cobrar depois é um control plane hospedado para times que não querem rodar o agendamento e o monitoramento por conta própria.

## Para devs, para gente de produto

Se você é dev, provavelmente já escreveu a versão frágil: um script de ingestão que funcionava até alguém renomear uma pasta, com uma lógica de re-embedding em que você nunca confiou de verdade. O Conduit é a permissão para apagar esse script. A tabela continua atual, as falhas ficam registradas e são tentadas de novo, e o seu tempo volta para a feature que você planejou construir.

Se você é de produto, a palavra que importa é frescor, porque frescor é qualidade de resposta. Um assistente lendo a tabela de preços do mês passado dá respostas erradas em tom confiante, e até agora o seu mecanismo de detecção era uma reclamação. O `status` do Conduit mostra cada fonte, cada execução e cada falha, e "a IA está errada porque o dado está velho?" vira uma pergunta com resposta em vez de um ticket de suporte com uma intuição.

## Construído do jeito que este blog prega

Este projeto saiu do mesmo loop que eu insisto em descrever: brainstorm, spec, plano, implementação, com [a spec como contrato](/pt-br/posts/2026-05-19-the-spec-driven-loop/) em cada etapa. As specs de design estão commitadas no repositório, ao lado do código que produziram. O time foi eu e o modelo, a mesma divisão de trabalho de sempre: a intenção e o julgamento foram meus, a estrutura e a execução foram do modelo.

Um tempo atrás eu argumentei que [uma ferramenta sob medida agora custa uma tarde](/pt-br/posts/2026-05-28-build-your-own-tools/). O Conduit é essa curva de custo levada adiante: um dev solo lançando um produto que antes exigia um time com funding, não porque a digitação ficou mais rápida, mas porque o loop aguenta tamanhos maiores. A spec de um produto é maior que a spec de uma ferramenta. Continua sendo uma spec.

## O que isso não é

- Não é um framework de RAG. O Conduit não recupera, não ranqueia, não monta prompt. Ele carrega e mantém fresco.
- Não é um vector database. Ele escreve no store que você já tem, começando pelo pgvector.
- Não é uma biblioteca de retrieval. Não há nada para importar. É um binário que roda.
- Não está pronto. É uma v1 com cinco tipos de fonte e um contrato de conectores aberto, construído para a comunidade ser dona da cauda longa de fontes.

## Experimente

Dois minutos com Docker: clone o [repositório](https://github.com/dynaum/conduit), aponte a config de exemplo para uma pasta e rode o sync. Depois rode de novo, e veja a segunda execução pular tudo. Esse pulo é o produto inteiro. O encanamento finalmente lembra o que já fez.
