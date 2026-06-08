---
title: "O Modelo Nunca Lê Suas Palavras"
subtitle: "Você digita em português. O modelo lê inteiros. Ele nunca vê uma única letra do que você escreveu. Entender a coisa no meio, o token, não é trivialidade. É a diferença entre chutar custo, contexto e design de prompt, e saber."
date: 2026-06-07
description: "Um LLM nunca vê o seu texto. Suas palavras são traduzidas em tokens, e depois em números, antes de o modelo tocar nelas. Uma explicação em linguagem simples do que é um token, e por que saber isso te torna melhor em custo, limites de contexto e design de prompt."
cover: /assets/img/2026-06-07-what-is-a-token.png
coverAlt: "Uma linha de texto âmbar brilhante dissolvendo-se da esquerda para a direita em um fluxo ascendente de numerais flutuantes, os dígitos iluminados por uma luz de borda azul-petróleo contra um fundo quase preto."
---

Você pode entregar uma funcionalidade inteira em cima de um LLM e nunca saber o que é um token. Eu fiz isso, por um tempo. Funciona até o momento em que o custo te surpreende, ou um prompt que parece curto estoura a janela de contexto, ou o modelo faz algo estranho e você não tem nenhuma teoria à mão para o porquê. Os três levam à mesma coisa que você pulou.

É o seguinte. O modelo nunca lê suas palavras. Você digita em português. O modelo lê inteiros. Ele não vê uma única letra do que você escreveu. Entre o seu texto e o modelo existe uma etapa de tradução, e é nessa etapa que mora a maioria das surpresas.

## O que é um token

Um token é um pedaço de texto. Muitas vezes uma palavra inteira. Muitas vezes parte de uma.

A tokenização é a etapa que divide o seu texto nesses pedaços. Pegue uma frase:

> O modelo nunca lê suas palavras.

Um tokenizador pode cortar isso em: `O`, ` modelo`, ` nunca`, ` lê`, ` suas`, ` palavras`, `.` Sete tokens. Repare que os espaços vão junto com as palavras, e o ponto final é o seu próprio token. Palavras comuns tendem a ser um único token. É por isso que texto curto e simples é barato.

Agora uma palavra mais rara:

> tokenização

Essa não é comum o suficiente para ganhar o próprio lugar, então é quebrada em pedaços, algo como `token` e `ização`. Uma palavra, dois tokens. O padrão se repete por toda parte. Palavras frequentes viram um token. Palavras raras, nomes, identificadores de código e grafias estranhas se dividem em vários.

É por isso também que modelos contam letras errado e tropeçam em palavras estranhas. O modelo nunca viu as letras. Ele viu alguns pedaços. Perguntar quantos r's existem em uma palavra é pedir que ele inspecione algo que nunca recebeu.

Uma proporção aproximada para guardar na cabeça: cerca de 750 tokens por 1000 palavras em inglês. Prosa simples fica perto disso. Quanto mais denso e estranho o seu texto, mais a contagem sobe.

## Do token para o número

Os pedaços ainda são texto, e o modelo não trabalha com texto. Então cada token é mapeado para um ID, um inteiro simples, tirado de uma lista fixa com a qual o modelo foi construído. Essa lista é o vocabulário, dezenas de milhares de entradas, cada uma um token com um número anexado.

Então a nossa frase deixa de ser palavras. Ela vira uma lista de inteiros, um por token. Algo como:

> `464`, `2746`, `2900`, `9743`, `534`, `2456`, `13`

Esses números exatos são ilustrativos, cada modelo tem o próprio vocabulário, mas o formato é real. Quando o seu prompt chega ao modelo, ele é uma fileira de inteiros. Nada de português. Só números no lugar dos pedaços.

## Do número para o significado

Um inteiro puro não carrega significado. `464` não é maior ou menor em sentido do que `2746`. Então mais uma etapa roda antes de o modelo raciocinar sobre qualquer coisa.

Cada ID de token vira um vetor, uma lista de números. Não um número, algumas centenas ou alguns milhares deles. Esse vetor é o embedding. Ele coloca o token em um espaço onde o significado tem geometria. Tokens que significam coisas parecidas ficam perto uns dos outros. Os vetores de `gato` e `cachorro` ficam mais próximos entre si do que os vetores de `gato` e `bicicleta`.

É aqui que o modelo de fato identifica a sua entrada. Não nas letras, que ele nunca viu. Não nos IDs inteiros, que são só rótulos. Nos embeddings, onde cada pedaço virou uma posição em um espaço sobre o qual o modelo pode fazer contas. Daqui o trabalho de verdade começa. Mas você já tem o que veio buscar.

## Por que você deveria se importar

Três coisas que você controla, todas com o formato do token.

**Custo.** Você paga por token, não por palavra. Então a unidade na sua conta é o pedaço, não a frase. Texto simples é denso em palavras comuns e barato. Código, JSON e dados estruturados são o oposto. Colchetes, aspas, indentação e identificadores longos custam tokens cada um, e somam rápido. Um payload que parece pequeno na tela pode ser o dobro dos tokens que você chutou.

**Contexto.** A janela de contexto é medida em tokens, nunca em palavras. Então um prompt que parece curto pode ser pesado. Cole um arquivo de configuração ou um stack trace e a contagem de tokens dispara, porque estrutura tokeniza mal. Quando você se perguntar como algumas telas de texto estouraram a janela, a resposta é essa. Você estava contando palavras. O modelo estava contando tokens.

**Design de prompt.** O modelo responde aos tokens que recebe, não às palavras que você imagina ter enviado. Formatação muda os tokens. Escolha de palavra muda os tokens. Até espaço em branco muda os tokens. É por isso que uma pequena reescrita às vezes desloca a saída mais do que deveria. Você não mudou a ideia. Você mudou os pedaços.

## Fechamento

Você não precisa contar tokens na mão. Você precisa abandonar a suposição que está por baixo das surpresas.

O modelo não lê português. Ele lê números, e o caminho das suas palavras até esses números é seu para projetar. Custo, contexto e comportamento do prompt deixam de ser um mistério no momento em que você enxerga a etapa de tradução que sempre esteve ali. As palavras são para você. Os tokens são para o modelo.
