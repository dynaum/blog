---
title: "Não Dê Root para o Seu Agente"
subtitle: "O MCP torna trivial conectar um agente aos seus dados. É exatamente por isso que a decisão de acesso virou a que importa: o que ele pode alcançar, o que ele pode fazer, e por que o menor privilégio é a única regra que se sustenta."
date: 2026-06-04
description: "Conectar um agente aos seus dados com MCP é a parte fácil. O trabalho de verdade são duas decisões de acesso, que dados o agente pode alcançar e o que ele pode fazer, ambas menor privilégio para um ator não humano. Com Redis como exemplo prático."
cover: /assets/img/2026-06-04-dont-give-your-agent-root.png
coverAlt: "Uma porta de cofre pesada numa parede de pedra escura, aberta só por uma fresta controlada com luz âmbar quente vazando pelo vão estreito, um mecanismo de fechadura iluminado em azul-petróleo em destaque no primeiro plano."
---

O post anterior foi sobre o agente como um sistema. Este é sobre as mãos dele.

Dar ferramentas a um agente já foi a parte difícil. Você escrevia uma integração customizada para cada ferramenta, cada modelo, cada banco de dados, e escrevia de novo quando qualquer um deles mudava. O MCP tornou isso trivial. E no momento em que a parte difícil fica trivial, uma parte diferente passa a ser a que importa, e a maioria das pessoas passa reto por ela.

## O que o MCP de fato é

O MCP, Model Context Protocol, é uma tomada padrão. A Anthropic o lançou como um protocolo aberto para como um agente se conecta a ferramentas e dados: um jeito definido de um servidor expor coisas que o agente pode ler e funções que o agente pode chamar, no mesmo formato não importa o que esteja por trás.

É isso tudo. O MCP é a tomada, não o aparelho e não a eletricidade. A ferramenta ainda é sua para construir. Os dados ainda são seus para escolher. Você pode colocar um servidor MCP na frente de uma API REST existente ou de um banco de dados existente sem mudar nenhum dos dois, e o servidor os traduz para coisas que o agente entende.

Uma ressalva honesta, porque ela importa mais adiante. A versão fácil é um wrapper fino que expõe cada endpoint e cada tabela. Essa versão também costuma ser a errada. Um bom servidor MCP faz curadoria. Ele expõe algumas ferramentas que fazem sentido para o agente, não toda a sua superfície. E no instante em que você faz curadoria, já está tomando uma decisão de acesso, percebendo ou não.

Então a conexão está resolvida. O que sobra é a parte que a tomada padrão torna fácil de errar: quanto dos seus dados o agente pode alcançar, e quanto ele tem permissão de fazer. Duas decisões. Um princípio.

## Que dados o agente precisa

Reduza os dados ao mínimo.

Um agente não precisa do seu banco de dados. Ele precisa da fatia que a tarefa exige. Mas o MCP torna expor tudo tão fácil quanto expor uma tabela, então o instinto é entregar a coisa inteira e deixar o agente descobrir o que é relevante. É o mesmo erro de um prompt vago. Uma superfície ampla convida ao vaguear. O agente puxa dados que não tinha razão de tocar, e os vaza por uma resposta que você não previu.

Decida o que o agente lê do jeito que você decide o escopo de uma conta de serviço. Nomeie as tabelas, os campos, as linhas que ele tem permissão de ver. A menor superfície de dados que dá conta do trabalho é a certa, pela mesma razão que é certa para um prestador de serviço humano. O que ele não alcança, ele não consegue usar errado.

## O que o agente pode fazer

Reduza os verbos, e barre os perigosos.

Ler é uma coisa. Agir é outra. Um agente que só lê é um risco que você consegue limitar. Um agente que pode escrever, apagar, fazer deploy ou gastar é um risco que você tem que barrar. Decida, por ferramenta, o que o agente pode fazer, não só o que ele pode ver. Os verbos destrutivos ganham uma etapa de aprovação humana, a regra do operador-no-loop, ligada na própria ferramenta em vez de deixada ao bom senso do agente.

Há uma razão mais afiada para a fronteira de acesso importar. Um agente age sobre entradas que você não escreveu: um documento que ele lê, uma página que ele busca, uma mensagem de usuário que pode carregar uma instrução escondida. O prompt pode ser subvertido. A permissão não, se você a definir direito. Quando uma entrada esperta convence seu agente a fazer algo estúpido, a única coisa entre o pedido e o estrago é o que você permitiu a ferramenta fazer já de início.

As duas decisões são o mesmo princípio antigo. Você não daria root a um prestador novo no primeiro dia. Você daria acesso de leitura ao único sistema de que ele precisa e um fluxo de solicitação para qualquer coisa destrutiva. Um agente é um prestador que nunca dorme, age em milissegundos, e faz exatamente o que o acesso dele permite, nem mais nem menos. O MCP não quebrou o menor privilégio. Ele só removeu o atrito que costumava impô-lo por acidente. Conectar tudo é uma config de distância agora, então a disciplina tem que ser uma decisão em vez de um efeito colateral.

## Coloque seus dados na frente, não os exponha

Aqui está uma forma concreta. Seus dados vivem num banco de dados primário, digamos Postgres. Você não aponta o agente para a produção.

Você coloca uma camada na frente. O [Redis Data Integration](https://redis.io/docs/latest/integrate/redis-data-integration/) mantém uma cópia no Redis em sincronia por change data capture, então o agente lê uma cópia rápida, atual e separada, em vez da sua fonte da verdade. O Redis então expõe essa cópia ao agente via MCP, com o [servidor MCP oficial do Redis](https://github.com/redis/mcp-redis), ou, com o mais novo motor de contexto [Redis Iris](https://redis.io/iris/), um retriever que gera ferramentas MCP escopadas sobre um modelo semântico dos seus dados.

O ponto não é o Redis. O ponto é a forma: uma camada controlada e escopada entre o agente e os seus dados reais, com as decisões de acesso tomadas nessa camada. Qualquer banco de dados com um caminho MCP pode fazer esse papel. O Redis é um que tem as peças hoje.

## O que isto não é

- Não é anti-MCP. O MCP é bom, e a conexão ser fácil é a vitória. Este post é sobre o que a vitória expõe.
- Não é um anúncio do Redis. O Redis é o exemplo prático porque as peças se encaixam, não porque é a única resposta. Coloque seus dados na frente com o que encaixar.
- Não é um paper de modelagem de ameaças. A injeção de prompt aparece aqui como uma razão para a fronteira importar, não como algo a dissecar. A fronteira é a defesa. Desenhá-la é o trabalho.

## Fechamento

A tomada é padrão agora. Isso é progresso de verdade, e significa que a decisão interessante se moveu. Não é mais como você conecta o agente aos seus dados. É o que você deixa ele alcançar e o que você deixa ele fazer uma vez conectado.

O modelo executa. Você decide. Com ferramentas, decidir significa desenhar a fronteira de acesso, porque essa é a única parte por onde um prompt esperto não consegue passar na conversa. Dê ao agente as chaves da única sala de que ele precisa. Não root.
