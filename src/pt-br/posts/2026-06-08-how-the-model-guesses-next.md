---
title: "Ele Só Adivinha a Próxima Palavra"
subtitle: "O modelo não decide o que dizer. Ele decide a próxima palavra, joga tudo de volta para dentro e decide de novo. O parágrafo que você lê como um pensamento foi construído um palpite de cada vez. Quando você enxerga o laço, três coisas deixam de ser um mistério."
date: 2026-06-08
description: "Um LLM não tem plano nem resposta guardada. Ele prevê um token, anexa ao final e roda a entrada inteira de novo. Esse único laço explica por que o mesmo prompt dá respostas diferentes, por que o modelo não consegue planejar adiante e por que a saída custa mais que a entrada."
cover: /assets/img/2026-06-08-how-the-model-guesses-next.png
coverAlt: "Um único ponto âmbar brilhante à esquerda estendendo-se em uma corrente de pontos mais fracos e repetidos para a direita, um motivo de laço iluminado por uma luz de borda azul-petróleo contra um fundo quase preto."
---

O modelo nunca decide o que dizer. Ele decide a próxima palavra. Depois joga o seu prompt inteiro e essa palavra nova de volta para dentro, e decide a próxima palavra. Depois faz tudo de novo. Um parágrafo que você lê como um único pensamento foi construído um palpite de cada vez, centenas de vezes, sem ideia no início de onde ia parar.

Essa é a parte que as pessoas pulam. Elas imaginam o modelo lendo a pergunta, pensando e escrevendo a resposta. O que ele de fato faz é rodar o mesmo passinho repetidamente. Quando você enxerga o laço, três coisas com que você briga todo dia deixam de ser um mistério.

## O laço

Seu texto vira tokens, depois números, depois vetores sobre os quais o modelo pode fazer contas. Esse é o caminho da entrada, e é onde a maioria das pessoas para de imaginar. Aqui está o que acontece em seguida.

O modelo pega essa entrada e produz uma coisa só: [uma probabilidade para cada token do seu vocabulário](https://arxiv.org/abs/2005.14165). Dezenas de milhares de números, cada um dizendo o quanto aquele token é provável de vir a seguir. Não a resposta. Só as chances do próximo token, um único.

Ele escolhe um. Cola esse token no final da entrada. Depois roda tudo de novo, agora um token mais longo, e produz um conjunto novo de chances para o token seguinte.

Esse laço é o ato inteiro da geração. Não existe um lugar dentro do modelo onde a resposta completa fica esperando. O modelo não tem ideia de qual será a sua terceira frase quando escreve a primeira palavra. Ele só calcula o próximo token, e a resposta é o que você obtém depois de o laço ter rodado algumas centenas de vezes. (O que deixa ele pesar a entrada inteira a cada passada se chama [atenção](https://arxiv.org/abs/1706.03762). Você não precisa do maquinário dela para usar nada disso.)

## Por que o mesmo prompt dá respostas diferentes

Se o modelo simplesmente pegasse o token mais provável toda vez, o mesmo prompt sempre daria a mesma resposta. Muitas vezes não dá, e agora você consegue ver por quê.

O modelo não é obrigado a pegar o token do topo. Ele [amostra das probabilidades](https://arxiv.org/abs/1904.09751). O token mais provável costuma vencer, mas um menos provável às vezes é escolhido, e essa única escolha muda todos os tokens que vêm depois.

A [temperatura](https://arxiv.org/abs/2402.05201) é o botão disso. Temperatura baixa empurra o modelo para a escolha do topo toda vez: focado, repetível e propenso a se repetir. Temperatura alta achata as chances, então tokens improváveis ganham uma chance real: mais variado, mais criativo, mais propenso a divagar. A aleatoriedade não é um defeito do modelo. É um ajuste que você controla.

## Por que ele não consegue planejar adiante

O modelo comete um token de cada vez, e não consegue voltar atrás em um token. Uma vez que uma palavra saiu, ela é parte da entrada para sempre, e todo token posterior precisa conviver com ela.

Então o modelo se escreve para dentro de cantos. Ele começa uma frase de um jeito, e três tokens depois não há um fechamento gracioso, mas ele não consegue revisar a abertura. Ele só consegue escolher o melhor próximo token diante da bagunça que já escreveu. Boa parte da saída desajeitada é o modelo preso a um caminho que não teria escolhido com previsão.

É também por isso que ["pense passo a passo"](https://arxiv.org/abs/2201.11903) funciona, e não é um truque. Todo token que o modelo gera vira entrada para a próxima passada. Quando você o faz escrever o raciocínio antes da resposta, esse raciocínio agora é contexto que os tokens finais conseguem usar como base. Você não está acordando um modelo mais inteligente. Você está dando ao laço mais material certo para se apoiar antes de ele se comprometer com a parte que te importa.

## Por que a saída custa mais que a entrada

Olhe qualquer tabela de preço de API e os tokens de saída custam mais que os de entrada. O laço explica.

A sua entrada é [lida em uma passada](https://arxiv.org/abs/2309.06180). O modelo ingere o prompt inteiro de uma vez e produz o primeiro conjunto de chances. A saída é o oposto. Cada token de saída é uma rodada separada do modelo, uma depois da outra, porque cada um depende do token anterior. Uma resposta de 500 tokens são aproximadamente 500 passadas sequenciais.

Esse trabalho sequencial é o custo. É por isso que a saída é mais cara, e por isso que uma resposta longa sai aos poucos e parece lenta enquanto um prompt longo é lido quase de imediato. Você está vendo o laço girar, um token por tique.

## Fechamento

Não existe uma resposta dentro do modelo. Existe um laço que adivinha o próximo token, e um conjunto de chances do qual ele amostra, e uma entrada que cresce um token a cada volta.

Tudo o que você guia mora nessa entrada. O que você coloca na frente do laço, quanto espaço você dá para ele raciocinar, quanta aleatoriedade você permite. O modelo roda o passo. Você molda com o que o passo tem para trabalhar. As palavras são para você. O laço roda em tokens.
