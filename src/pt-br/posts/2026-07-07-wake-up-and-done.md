---
title: "Quando Eu Acordo, e Quando Eu Termino?"
subtitle: "Toda execução autônoma responde a duas perguntas. O /loop responde uma, o /goal responde a outra, e o problema começa quando você faz uma fingir o trabalho das duas."
date: 2026-07-07
description: "Um agente deixado rodando enfrenta duas decisões separadas a cada turno: quando acordar, e quando parar. O /loop é um relógio. O /goal é um avaliador novo checando uma condição. Cada um tem um ponto cego que é exatamente a força do outro. Veja como casar o comando com a pergunta."
cover: /assets/img/2026-07-07-wake-up-and-done.png
coverAlt: "Uma parede de oficina em carvão profundo com dois instrumentos, um relógio de parede âmbar quente brilhando à esquerda e uma única luminária acesa sobre uma linha de chegada marcada na bancada, luz de contorno em teal suave, textura de pincelada e brilho difuso."
---

Deixe um agente rodando e ele enfrenta duas perguntas a cada turno. Quando eu acordo. Quando eu termino.

Elas parecem uma pergunta só. Não são. Uma é sobre cadência. A outra é sobre a linha de chegada. O Claude Code dá um comando separado para cada uma, e o problema começa no momento em que você faz uma fazer o trabalho da outra.

## Duas perguntas, não uma

Qualquer execução que continua sem você mandar a cada passo precisa decidir duas coisas. O que inicia o próximo turno. O que encerra o trabalho. Um cron responde à primeira e nunca à segunda. Uma checklist responde à segunda e não diz nada sobre tempo. Um agente precisa das duas respondidas, e elas puxam em direções diferentes.

Nomeie-as com clareza. Cadência: com que frequência eu volto. Conclusão: como eu sei que devo parar. Mantenha-as separadas na sua cabeça e o comando certo para cada uma aparece sozinho.

## A linha de chegada

O [`/goal`](https://code.claude.com/docs/en/goal) define uma condição de conclusão. Depois de cada turno, um modelo pequeno e rápido lê a conversa e decide se a condição vale. Se não valer, o Claude toma outro turno por conta própria. A meta se encerra quando a condição é atingida. O próximo turno dispara no instante em que o último termina, então o trabalho corre em sequência, sem esperar por um relógio.

```text
/goal all tests in test/auth pass and the lint step is clean
```

O ponto cego vale ser dito em voz alta. O avaliador lê a transcrição. Ele não roda nenhuma ferramenta. Não abre um arquivo nem roda um teste sozinho. Então escreva a condição como algo que a própria saída do Claude prova. "Todos os testes em test/auth passam" funciona, porque o Claude roda os testes e o resultado cai na transcrição para o avaliador ler. "O serviço está saudável em produção" não funciona, porque nada na conversa mostra isso.

A força: o juiz é um modelo novo, não o que fez o trabalho. A conclusão é decidida por um segundo par de olhos.

## O relógio

O [`/loop`](https://code.claude.com/docs/en/scheduled-tasks) roda de novo um prompt em um cronograma. Dê um intervalo e ele dispara nessa cadência. Omita o intervalo e o Claude escolhe o atraso a cada rodada, curto enquanto um build está terminando, longo quando as coisas ficam quietas. Um loop continua até você parar ou até o Claude decidir que o trabalho acabou.

```text
/loop check whether CI passed and address any review comments
```

O ponto cego espelha o da meta. O modelo que faz o trabalho é o mesmo que decide que ele terminou. O executor corrige a própria prova. Tudo bem para um monitoramento onde o "terminou" é óbvio. Fraco para trabalho de verdade, onde a linha de chegada é uma afirmação que você quer checada por alguém que não seja quem a fez.

A força: um loop é dono do relógio. Ele espera, ele volta, ele se ritma contra o mundo lá fora.

## Cada lacuna é o trabalho da outra

Coloque os dois pontos cegos lado a lado e o padrão é difícil de ignorar.

Uma meta não consegue esperar pelo mundo lá fora. Nada faz o relógio andar a não ser um turno concluído, e o avaliador só enxerga o que está escrito. Um loop não julga bem a conclusão, porque o juiz e o executor são o mesmo modelo.

Agora leia as forças cruzadas. Um loop é dono do relógio que falta à meta. Uma meta é dona do juiz novo que falta ao loop. A lacuna de um é o propósito inteiro do outro.

## Uma execução, as duas perguntas

Digamos que você suba um branch e queira ele verde e mesclado sem babá. Dois relógios estão rodando. O seu, e o da CI. A CI termina no cronograma dela, daqui a alguns minutos, e nada na sua sessão move isso. Esta é a fase de espera, e ela pertence ao loop. O Claude acorda na própria cadência, lê a execução, espera mais tempo quando o branch fica quieto.

Aí a CI volta vermelha. O trabalho vira para dentro. Agora cada pedaço de estado vive na transcrição: o log que falhou, a correção, a nova execução. Esta é a fase de fechamento, e ela pertence à meta. Defina a condição. Todo job neste branch está verde e o git status está limpo. O Claude mói turno após turno, e um modelo novo confirma o fim, no lugar do modelo que escreveu a correção.

Uma tarefa real tem as duas fases. A habilidade é nomear em qual delas você está e alcançar o comando que serve. O loop faz a ponte com o mundo lá fora. A meta conduz até um fechamento checado. Nenhum dos dois faz as duas coisas bem.

## As arestas honestas

Alguns limites, para que nada te pegue de surpresa. Uma meta por sessão, então é uma linha de chegada por vez. O avaliador da meta nunca roda ferramentas, então uma condição que ele não consegue ler na transcrição nunca vai registrar como atingida. Um loop dispara só enquanto a sessão está aberta e ociosa, então feche o terminal e o relógio para. Loops expiram sozinhos depois de sete dias.

Há uma terceira peça silenciosa embaixo das duas. O modo automático aprova chamadas de ferramenta dentro de um turno, então cada turno roda sem supervisão. Ele não inicia o próximo turno. Meta e loop iniciam turnos. O modo automático deixa cada turno correr sem parar para perguntar. Você quer os três para um trabalho de fato sem as mãos.

## Fechamento

Antes de soltar uma execução, pergunte qual pergunta você está respondendo. Você precisa de uma cadência, ou de uma linha de chegada. Se o trabalho espera por algo fora da sessão, você precisa de um relógio, e isso é o `/loop`. Se o trabalho tem um estado final que o Claude consegue provar na própria saída, você precisa de um juiz, e isso é o `/goal`. A maioria das tarefas guarda um trecho de cada.

Nomeie a pergunta primeiro. O comando vem depois.
