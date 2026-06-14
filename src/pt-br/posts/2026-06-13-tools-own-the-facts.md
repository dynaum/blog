---
title: "Não Faça o Modelo Executar uma Etapa de Build"
subtitle: "Um agente gasta os primeiros minutos de cada sessão reconstruindo um mapa do seu código. Um script já tem esse mapa. O modelo deveria ler os fatos, não redescobri-los."
date: 2026-06-13
description: "O contexto de que um agente precisa se divide em fatos e julgamento. Um grafo de código, a superfície de API e o mapa de dependências podem ser gerados a partir do código-fonte e mantidos atualizados a cada commit. Pedir a um LLM para produzi-los ou mantê-los é mais lento, custa tokens e apodrece. Deixe a etapa de build dona dos fatos e guarde o modelo para o julgamento."
cover: /assets/img/2026-06-13-tools-own-the-facts.png
coverAlt: "Uma cena em carvão profundo onde um diagrama de fiação âmbar brilhante se desenha sozinho ao longo de linhas precisas de luz azul-petróleo, sem mão humana no quadro, textura de pincelada e brilho suave."
---

Observe um agente começar uma tarefa em um código que ele já viu antes. Ele faz um grep por uma função. Abre três arquivos para descobrir o que chama essa função. Lê um import para achar onde um tipo está definido, depois abre aquele arquivo também. Cinco minutos depois, ele reconstruiu um mapa do seu código na cabeça. O mesmo mapa que reconstruiu ontem. O mesmo mapa que um script teria entregado em dois segundos.

Você paga por isso. Tokens para cada arquivo que ele lê para se orientar. Latência enquanto ele vagueia. E pior que o custo, você confia em um palpite onde poderia ter um fato. O modelo mental que o agente faz do seu código é uma inferência. O código em si é a verdade.

Esse é o erro que eu quero nomear. Recorremos ao modelo para um trabalho que uma etapa de build faz melhor.

## Fatos e julgamento

O contexto de que um agente precisa vem em dois tipos.

Um tipo são os fatos sobre o código. Onde isto está definido. O que o chama. O que esta API aceita e retorna. Quais módulos dependem de quais. O que está obsoleto. Essas respostas vivem no código-fonte. Não são opiniões. Uma ferramenta as lê.

O outro tipo é o julgamento. Dados esses fatos, e dado o que estamos tentando construir, qual mudança faz sentido. Esse é o trabalho do modelo, e o modelo é bom nisso.

A linha entre os dois é nítida, e a maioria das configurações a borra. Elas fazem o modelo coletar os fatos antes de poder pensar. O modelo é mais lento que um parser para coletar, mais caro, e esquece tudo no instante em que a sessão acaba. Aí ele faz tudo de novo na próxima vez.

## Os três determinísticos

Três mapas cobrem a maior parte daquilo que um agente reorienta, e todos os três saem do código-fonte sem nenhum modelo no caminho.

Um **grafo de código**. Quem define cada símbolo, quem o chama, o que importa o quê. Um parser percorre a árvore de sintaxe e anota. Esse é o mapa que o agente reconstrói à mão a cada sessão. Construa uma vez por commit no lugar disso.

Uma **superfície de API**. Os tipos públicos, as assinaturas de função, as rotas, o schema do banco. O contrato que seu código expõe. Você não narra um contrato para um agente torcendo para ele continuar atualizado. Você o deriva dos tipos que já existem e o regenera quando eles mudam.

Um **mapa de dependências e arquitetura**. Os limites entre módulos, para que lado as dependências apontam, o que está saindo. Esse pega os erros mais confiantes do agente, a mudança que parece certa em um arquivo e quebra a estrutura de camadas do sistema inteiro. Gerado a partir dos imports e da configuração, ele é um fato que o agente lê em vez de uma regra na qual tropeça.

Nenhum desses precisa de um modelo de linguagem para ser produzido. Precisam de um parser e de um hook de commit. A saída é um arquivo que o agente lê primeiro, atualizado toda vez, porque uma etapa de build o reescreveu quando o código mudou pela última vez.

## O único mapa que uma ferramenta não constrói

Há um limite, e ele prova a regra.

Uma ferramenta consegue ler o seu código. Não consegue ler a sua intenção. Por que esta funcionalidade existe, o que conta como pronto, o que você decidiu não construir e por quê. Isso vive nas cabeças, não no código, e nenhum parser jamais vai encontrar. Eu já [escrevi](/pt-br/posts/2026-05-24-context-is-not-a-dev-job/) sobre [essa metade](/pt-br/posts/2026-05-22-your-ai-context-belongs-to-the-team/) antes. Um humano escreve a visão de produto, uma vez, à mão.

Então o agente recebe duas entradas. Os fatos, derivados do código por uma ferramenta. A intenção, escrita por uma pessoa. As duas chegam atualizadas, nenhuma cabe ao modelo inventar. O modelo fica no meio e faz a única coisa que só ele faz. Ele raciocina.

Repare no que o modelo nunca faz nessa cena. Ele nunca produz os fatos. Nunca produz a intenção. Ele consome os dois e escreve a mudança.

## Por que a etapa de build vence

Três razões, e elas se somam.

Custo. Um mapa gerado são alguns segundos de CPU. O agente lendo o mesmo mapa à mão são dezenas de leituras de arquivo, a cada sessão, pagas em tokens toda vez.

Velocidade. O mapa já está no disco quando o agente começa. Sem fase de orientação. Ele abre um arquivo e conhece o formato do sistema.

Confiança, e essa é a que mais importa. Um mapa gerado não tem como ficar desatualizado, porque um hook de commit o reescreve sempre que o código muda. O modelo mental de um LLM envelhece no instante em que um colega faz um merge. Um documento que uma pessoa escreveu no trimestre passado já está mentindo. A única documentação em que você confia é a que um pipeline regenera, a mesma razão pela qual construí o [Conduit](/pt-br/posts/2026-06-12-conduit-launch/) para manter os dados de recuperação atualizados em vez de confiar num retrato. A atualização vem de um pipeline, não de um autor.

## O que isto não é

- Não é um tutorial de ferramentas. Tree-sitter, ctags, language servers, geradores de OpenAPI, a categoria está cheia de boas opções e elas não são o ponto. Escolha uma.
- Não é anti-LLM. O modelo é a razão inteira de fazer isso. Você está limpando a mesa dele para que ele possa pensar.
- Não é o argumento do contexto humano de novo. Aquele era sobre escrever a intenção. Este é sobre não escrever fatos que uma ferramenta já conhece.

## Fechamento

Pare de pedir ao modelo para ser uma versão pior de uma etapa de build. Ele é lento para coletar, esquece entre as sessões e adivinha onde um parser saberia.

Dê a ele um mapa que a etapa de build mantém atualizado e uma intenção que uma pessoa escreveu. Aí deixe ele fazer a parte para a qual você de fato o contratou.
