---
title: "Você Não Consegue Escrever um Arquivo de Contexto para uma Pessoa"
subtitle: "Todo fato sobre meus sistemas mora em um arquivo que o agente carrega quando precisa. O sinal que eu preciso para gerir uma pessoa é aquilo que nunca aconteceu, e o que falta não vira token."
date: 2026-09-14
description: "Feedback resiste à automação por um motivo estreito e mecânico: a entrada dele é ausência. Notas de campo sobre ler pessoas, confrontar do jeito certo, e por que o momento da IA deixou as duas coisas mais difíceis."
cover: /assets/img/2026-09-14-context-file-for-a-person.png
coverAlt: "Duas cadeiras de madeira vazias sob uma única lâmpada pendente em uma sala escura e esverdeada, uma pilha de páginas escritas no chão ao lado de uma delas, logo fora da luz."
---

Eu já escrevi arquivos de contexto para meus repositórios, meus passos de deploy, meus usuários. Nunca consegui escrever um para uma pessoa.

Todos esses arquivos funcionam do mesmo jeito. Eu sei um fato, escrevo uma vez, e [toda sessão depois disso carrega ele de graça](/pt-br/posts/2026-06-15-commit-the-context/). A técnica é chata e nunca me falhou em um sistema.

No mês passado eu tinha uma conversa difícil pela frente. Um engenheiro cujo trabalho tinha caído de nível, e três semanas de mim adiando falar isso. Então fiz o que faço com toda coisa difícil. Abri uma sessão e pedi ajuda para me preparar.

Veio uma página. A estrutura estava certa. Abrir com o comportamento específico, separar o trabalho da pessoa, perguntar antes de afirmar, fechar com um próximo passo concreto. Profissional e defensável. Li duas vezes e não usei uma frase sequer.

Tentar não foi uma ideia burra. Feedback parece trabalho de padrão quando visto de fora. Existem frameworks para isso. Existe um formato de conversa boa, e modelos são excelentes em formato.

## A entrada nunca esteve lá

O motivo da falha é estreito e mecânico. Eu não tinha nada para colocar dentro.

Isto é o que eu vinha lendo por três semanas.

Ele parou de fazer perguntas em design review. Ele era a pessoa que achava o buraco do plano no slide quatro. Por um mês, concordou com tudo.

Um pull request que nunca abriu. Ele disse que pegava o trabalho de migração. Nunca recusou. Nunca apareceu nada.

"É, tá tranquilo." Quatro palavras, no fim de uma call, sobre um refactor que ele tinha defendido com força duas semanas antes.

Agora liste o que um modelo tinha acesso. Os pull requests que ele abriu. Os tickets que ele fechou. Transcrições de reunião, se eu colasse lá. Tudo presente, tudo em ordem. Cada artefato mostrava um engenheiro tendo um trimestre normal.

O sinal não estava em nenhum deles. O sinal era a pergunta que ele não fez. Uma ferramenta lê o que está ali. Gerir lê o que está faltando, e uma coisa que não aconteceu não deixa nada para trás para ser escrito. Não existe arquivo, porque não existe fato.

## Ler nas entrelinhas é histórico, não instinto

As pessoas chamam isso de intuição, o que faz soar como um dom que você tem ou não tem.

É um diff. Eu sei como essa pessoa soa quando está tudo bem, porque tenho seis meses dele estando bem. A linha de base não mora em lugar nenhum além de mim, construída em salas sem nada de especial, semana após semana. Quando uma semana nova chega diferente da linha de base, a diferença é a mensagem inteira.

É por isso que um gestor novo não consegue ler um time na primeira semana, e alguém de fora nunca lê. Não é falta de habilidade. É falta de linha de base. Você precisa estar presente nos meses chatos para entender o mês interessante.

## Depois você ainda precisa dizer algo

Suponha que você leu certo. A parte difícil começa depois.

Tenho dois engenheiros em mente. Para o primeiro eu digo "isso não é o seu melhor trabalho" e ele fica mais afiado até quinta. Ele quer a régua alta e ouve franqueza como respeito. Diga as mesmas palavras para o segundo e ele fica calado em design review por um mês, e eu gasto seis semanas reconquistando a sala. Com ele a frase precisa chegar como pergunta. "Me explica o tradeoff aqui." Mesma preocupação, mesma semana, mesmo objetivo, frase oposta.

Nada na situação diz qual das duas pessoas está na sua frente. Você aprende do jeito caro, errando com aquela pessoa específica e pagando por isso. E o custo não é um retry. Um prompt ruim desperdiça um minuto. Uma frase mal mirada custa um mês da confiança de alguém.

## O momento da IA deixou isso mais difícil, não mais fácil

As ferramentas achataram a saída. O pull request de um júnior hoje lê como o de um sênior. Formatado, testado, mensagem de commit limpa, estrutura sensata.

Por anos aquela superfície foi um sinal de graça. Dava para saber quem estava pensando, quem estava com dificuldade e quem estava pronto para mais, só lendo o trabalho. Esse sinal ficou mudo.

Então a leitura desceu para baixo, para julgamento e intenção. Por que essa abordagem. O que a pessoa escolheu não fazer. Se ela entendeu o que entregou ou [aceitou o que o modelo entregou para ela](/pt-br/posts/2026-07-14-not-the-model/). Nada disso vem com ferramenta junto. Quem está aprendendo a gerir agora tem menos sinais de graça para praticar do que eu tive, e ninguém avisou que os sinais sumiram.

Chamamos isso de soft skills, o pior nome da nossa indústria. Soa opcional e vagamente parecido com ser gentil. É técnica. Qual frase, qual semana, qual sala, e se você [conquistou o direito de dizer aquilo](/pt-br/posts/2026-05-21-you-cannot-push-a-developer/).

## Onde o modelo ajuda de verdade

Eu ainda uso IA em volta desse trabalho, então deixa eu ser exato sobre onde.

É um bom parceiro de ensaio. Escrevo a primeira versão injusta do que quero dizer, aquela com a minha frustração ainda dentro, e pergunto quais partes chegam como ataque. Útil, todas as vezes. Depois jogo o rascunho fora.

Ele me pega sendo vago. "Melhore sua comunicação" é uma frase sem comportamento nenhum dentro, e ouvir isso antes da reunião em vez de durante vale o custo dos tokens.

O que ele não tem é ele. Ele tem a minha descrição dele, que é a minha leitura, já filtrada por tudo que eu entendi errado. Pedir para ele confirmar a minha leitura é pedir segunda opinião para um espelho.

Todo mundo vai aprender essas ferramentas. Essa diferença fecha rápido e fecha sozinha. Em dois anos, tocar um agente bem vai ser o básico, do mesmo jeito que usar um debugger é hoje.

A parte que não se nivela é a parte sem arquivo por trás. Notar a pergunta que parou de ser feita. Saber qual das duas frases usar numa terça. Errar sobre uma pessoa, e continuar na sala depois.

Eu commito todo o resto. Nunca achei um jeito de commitar isso.
