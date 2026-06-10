---
title: "Ele Nunca Sabe Que Não Sabe"
subtitle: "Não existe um momento dentro do modelo em que ele saiba que não sabe. A mesma máquina que te dá uma resposta certa te dá uma errada com a mesma confiança, e por dentro as duas são idênticas. Alucinação não é um modo quebrado. É o modo normal, em terreno fraco."
date: 2026-06-09
description: "Alucinação não é um bug separado em um LLM. É a máquina de próximo token rodando onde o apoio do treinamento é fino. Mesma engrenagem, terreno mais fraco. Por que o tom confiante não é um sinal, onde o modelo falha de forma previsível e por que a verificação precisa morar fora dele."
cover: /assets/img/2026-06-09-it-never-knows-it-doesnt-know.png
coverAlt: "Uma forma âmbar sólida e brilhante à esquerda esfarelando-se em partículas incertas e espalhadas em direção à borda direita, um núcleo confiante dissolvendo-se em dúvida, iluminado por uma luz de borda azul-petróleo contra um fundo quase preto."
---

Não existe um momento dentro do modelo em que ele saiba que não sabe. Ele não chega na beira do que tem e sente o abismo. Ele produz uma resposta do mesmo jeito toda vez, e a resposta que está certa e a resposta que está errada com confiança saem exatamente da mesma máquina, exatamente com a mesma voz. Por dentro, não há nada que as diferencie.

A gente chama as erradas de alucinações, como se o modelo tivesse escorregado para um modo quebrado. Não escorregou. Ele estava rodando normalmente o tempo todo. Alucinação não é um defeito parafusado em um sistema que funciona. É o sistema que funciona, de pé em terreno fraco.

## Por que acontece

O modelo prevê um próximo token plausível. Ele não tem um depósito de fatos para consultar, nenhum banco de dados onde busca respostas. O que ele tem é uma compressão de padrões do treinamento, e a partir disso produz chances do que vem a seguir.

Onde o treinamento deu um apoio forte e repetido, o token plausível é quase sempre o verdadeiro. Pergunte de que cor é o céu e o caminho está liso de tanto ser percorrido por dez mil exemplos. A resposta provável e a resposta correta são o mesmo token.

Agora peça a população exata de uma cidade pequena, ou o título de um artigo específico, ou o que aconteceu na semana passada. O modelo ainda produz um token plausível, porque produzir um token plausível é a única coisa que ele faz. Mas o chão embaixo desse palpite é fino, e plausível já não é o mesmo que verdadeiro. A máquina não mudou. O apoio mudou. Essa lacuna, entre o que soa certo e o que é certo, é a alucinação. Mesma engrenagem, terreno mais fraco.

## Confiança não é um sinal

Aqui está a armadilha. O tom fluente e seguro da resposta é gerado pelo mesmo laço que os fatos dentro dela. O modelo não escreve o conteúdo e depois adiciona confiança por cima. A confiança está nos tokens, prevista junto com todo o resto. Uma frase suave e segura é tão barata de produzir quando está errada quanto quando está certa.

Então o tom não te diz nada. Você não consegue ler a certeza na prosa, porque a prosa está sempre certa. Esse é o registro padrão dela.

E você não consegue obter a dúvida pedindo por ela. "Você tem certeza?" não consulta um medidor de confiança interno. Só entrega ao modelo um novo prompt, e o modelo gera uma resposta plausível para esse também. Muitas vezes ele recua e se desculpa quando estava certo. Às vezes ele insiste quando estava errado. Nenhuma das respostas é um relatório sobre o próprio estado, porque não há estado para relatar. A dúvida nunca foi representada. Você não consegue recuperar o que nunca esteve lá.

## Onde ele falha é previsível

A boa notícia é que terreno fino é previsível. Você consegue adivinhar de antemão onde o modelo está sobre uma base sólida e onde não está.

Terreno sólido é conhecimento comum, repetido e estável. O tipo de coisa que apareceu do mesmo jeito em quantidades enormes de texto. Terreno fraco é tudo que é específico e incomum: números exatos, nomes de pessoas que não são famosas, citações e fontes, datas, eventos recentes, os detalhes precisos de qualquer coisa de nicho. Quanto mais preciso e mais obscuro o pedido, mais fino o apoio, maior a invenção.

Isso te dá uma regra prática. Quanto mais suave e geral a pergunta, mais você pode se apoiar na resposta. Quanto mais ela se estreita para um fato específico que você poderia procurar, mais você deveria tratar a resposta como um rascunho a conferir, não um resultado a confiar. Você não precisa se surpreender com onde ele falha. Você consegue prever.

## A verificação mora fora do modelo

Você não conserta isso com um prompt melhor. Não existe frase que transforme plausível em verdadeiro, porque o modelo não tem acesso ao verdadeiro. O conserto é colocar a verdade onde o modelo possa usá-la, e conferir a saída onde o modelo não alcança.

Colocar a verdade ao alcance significa ancorar o laço em algo real. Dê ao modelo o documento de verdade, o registro de verdade, o resultado de uma chamada de ferramenta de verdade, dentro do contexto. Quando o fato real fica na frente do laço, o token verdadeiro vira o de alta probabilidade, e o modelo cavalga a sua evidência em vez das suas premissas finas. É só isso que a recuperação é. Não é mágica, só empilhar as chances a favor da resposta que você consegue sustentar.

Conferir a saída significa verificar contra uma verdade que mora inteiramente fora do modelo. Uma fonte, um banco de dados, um teste, uma pessoa que sabe. O modelo propõe. A verdade é confirmada em algum lugar que ele não alcança.

## Fechamento

O modelo te dá plausível. Sempre, por construção, sendo ou não plausível verdadeiro desta vez. Ele nunca vai parar na beira do seu conhecimento e te dizer que acabou, porque ele não sabe onde fica a beira.

Essa parte é sua. Forneça a verdade, ou verifique-a. O laço roda em chances, e chances não são fatos. A fluência é de graça. A precisão você tem que construir.
