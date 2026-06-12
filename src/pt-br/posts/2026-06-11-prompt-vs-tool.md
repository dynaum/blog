---
title: "O Que Vai no Prompt, O Que Vai na Ferramenta"
subtitle: "Um agente guarda seu conhecimento em dois lugares, e a maioria dos agentes quebrados tem algo do lado errado. Uma pergunta decide a divisão: isso muda entre as chamadas? Não: prompt. Sim: ferramenta."
date: 2026-06-11
description: "Onde o conhecimento do agente deve morar: regras, papel e vocabulário estáveis no prompt, dados e estado vivos atrás de ferramentas. Os dois modos de falha espelhados (fotografias velhas no prompt, comportamento condicional enterrado em ferramentas) e o teste de uma pergunta que corrige os dois."
cover: /assets/img/2026-06-11-prompt-vs-tool.png
coverAlt: "Uma bancada escura dividida ao meio. À esquerda, um contrato de papel desgastado e fixado brilha em âmbar quente. À direita, uma fileira de ferramentas penduradas recebe uma luz de contorno azul-petróleo."
---

Um agente guarda o que sabe em dois lugares. O prompt, que ele lê a cada turno. E as ferramentas, que ele chama quando decide chamar. Cada pedaço de conhecimento que você entrega a um agente cai de um lado ou do outro, e a maioria dos agentes quebrados que eu vejo está quebrada porque algo caiu do lado errado.

As falhas parecem não ter relação. Um agente cita um preço da terça passada. Outro segue a política de reembolso em alguns turnos e a ignora em outros. Mesmo erro, espelhado. Veja como ele aparece de perto.

## Versão um: dados vivos no prompt

Imagine um agente de suporte a pedidos de uma loja pequena. No dia do build, o desenvolvedor cola o catálogo no system prompt. Nomes de produtos, preços, o que tem em estoque. A demo fica ótima. O agente sabe tudo, responde na hora, nunca faz uma chamada de ferramenta. Pode lançar.

Na sexta ele mente. Os preços mudaram na quarta. A luminária azul esgotou na quinta. O agente continua citando a fotografia de segunda, e faz isso com total confiança, porque nada no contexto dele diz que os dados envelheceram. Um modelo [responde a partir do que está na frente dele](/pt-br/posts/2026-06-09-it-never-knows-it-doesnt-know/) e não tem canal para "esse número está velho". Texto no prompt não carrega timestamp que o modelo respeite. Para o modelo, é tudo igualmente verdadeiro, para sempre.

Dado vivo colado num prompt é uma fotografia pregada sobre uma janela. Parece a vista. Já foi a vista, um dia.

## Versão dois: comportamento enterrado na ferramenta

Então o desenvolvedor corrige. Estoque e preços vão para trás de uma ferramenta de consulta. O agente chama, recebe números frescos, a mentira para. E, enquanto liga a ferramenta de reembolso, o desenvolvedor coloca a política de reembolso onde pareceu natural: dentro da ferramenta. O limite de trinta dias, a exigência de nota, as exceções, tudo escrito no retorno da ferramenta, o lugar que o agente vê quando vai procurar.

Agora o comportamento é condicional. Nos turnos em que o agente consulta a ferramenta de reembolso, ele conhece a política e segura a linha. Nos turnos em que o cliente é persuasivo e o agente conclui sozinho que "esse caso obviamente está ok" sem tocar na ferramenta, a política não existe. O agente concede um reembolso fora da política, educado e confiante, exatamente no turno em que a regra deveria valer.

Uma regra que o agente precisa seguir em todo turno não pode morar num lugar que o agente visita em alguns turnos. Comportamento dentro de ferramenta é um contrato guardado na gaveta.

## A regra

Para cada pedaço de conhecimento, faça uma pergunta: isso muda entre as chamadas?

Não: vai no prompt. O papel do agente, as políticas, o vocabulário, o tom, os limites. As coisas verdadeiras em todo turno, para todo cliente, até você mudar de propósito. Esse é o [prompt como contrato](/pt-br/posts/2026-06-03-agents-are-systems-not-prompts/), e um contrato só funciona se estiver presente toda vez que o agente age.

Sim: vai para trás de uma ferramenta. Estoque, preços, estado do pedido, histórico da conta, a agenda de hoje. Qualquer coisa com timestamp. O agente busca na hora do uso e recebe a verdade atual em vez de uma fotografia.

A economia concorda com a correção. Texto de prompt é um custo pago em toda chamada, então o conhecimento ganha o assento ali quando é necessário em toda chamada. Uma ferramenta custa tokens só quando usada. Erre a colocação para um lado e você paga todo turno por um dado que já está envelhecendo. Erre para o outro e você economiza tokens tornando suas regras opcionais.

## A terceira prateleira

Uma complicação honesta. Parte do conhecimento é estável mas grande demais para viajar em todo prompt. O manual completo do produto. Um guia de estilo. A documentação de uma codebase. Muda raramente, então pela regra seria material de prompt, mas nesse tamanho afogaria o contexto.

Esse conhecimento vai para uma terceira prateleira: retrieval. Buscado como ferramenta, consumido como prompt. Pipelines de RAG fazem isso, e também os arquivos de skill que um agente carrega quando a tarefa pede. O teste ganha uma cláusula. Estável e pequeno: prompt. Estável e grande: texto recuperado. Mutável: ferramenta. Essa é toda a extensão, e os detalhes são um post próprio.

## O que isso não é

- Não é um explicador de RAG. Retrieval ganha uma prateleira aqui, não uma arquitetura. Sem chunking, sem embeddings.
- Não é sobre acesso. O que o agente pode alcançar e fazer é [uma decisão própria com post próprio](/pt-br/posts/2026-06-04-dont-give-your-agent-root/). Este post decide onde o conhecimento mora, não o que o agente pode tocar.
- Não é engenharia de prompt. Sem truques de frase. Uma política perfeitamente escrita no lugar errado continua falhando.

## Fechamento

O prompt é o contrato. As ferramentas são as mãos. O contrato guarda o que é sempre verdadeiro. As mãos buscam o que é verdadeiro agora.

A maioria dos agentes que se comportam mal não está sem conhecimento. Eles o têm do lado errado dessa linha, uma fotografia fazendo o trabalho de uma consulta, ou uma regra trabalhando só quando convocada. Classifique cada pedaço de conhecimento pela taxa de mudança e a linha se desenha sozinha.
