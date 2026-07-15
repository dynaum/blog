---
title: "O Modelo Nunca Foi o Gargalo"
subtitle: "Você deu Claude e Copilot para todo mundo e o time entrega na mesma velocidade. A ferramenta fez o trabalho dela. Ela tornou a escrita de código quase gratuita e deixou todos os custos mais lentos, os que você nunca cronometrou, exatamente onde sempre estiveram."
date: 2026-07-14
description: "Empresas adotam ferramentas de IA para código e esperam a entrega acelerar. Muitas vezes não acelera. O modelo derrubou o custo de escrever código e expôs os gargalos reais que ficam antes dele: reuniões que deveriam ser specs, conhecimento preso em uma cabeça, contratos que ninguém escreveu, intenção vaga. Um diagnóstico, e um teste para rodar na sua própria semana."
cover: /assets/img/2026-07-14-not-the-model.png
coverAlt: "Uma única mesa iluminada em primeiro plano onde papelada e pastas se acumulam sob uma luminária âmbar quente, uma pessoa esperando ao lado, enquanto atrás dela uma linha de montagem automatizada e brilhante corre rápida e vazia rumo à escuridão, luz de contorno azul-esverdeada, textura de pincelada e brilho suave."
---

Três meses depois da adoção, um líder fala em voz alta: "Demos Claude para todo mundo. Por que não estamos entregando mais rápido?"

É uma pergunta justa. A licença está paga, as ferramentas estão em todo editor, as demos eram reais. E o burndown parece igual ao do trimestre passado. A resposta incômoda é que a ferramenta funcionou exatamente como prometido, e a promessa era menor do que qualquer um mediu.

## Você nunca passou a maior parte do tempo escrevendo código

Imagine uma feature normal. Cinco dias da ideia ao merge. Parece cinco dias de engenharia, porque engenharia é a parte visível, a parte com uma pessoa num editor parecendo ocupada.

Agora observe para onde os cinco dias realmente vão. Um dia são três reuniões para decidir o que construir. Meio dia é esperar a única pessoa que entende o módulo de faturamento responder uma mensagem no Slack. Meio dia é caçar um contrato de API que ninguém escreveu. Dois dias são escrever e depurar o código. Um dia é o pull request parado numa fila de revisão.

Codar eram dois dos cinco dias. A IA corta esses dois dias para uma tarde. Você economizou um dia e meio. Os outros três dias e meio não se moveram, e agora são todo o custo visível. O time não está mais lento. Você finalmente está enxergando para onde o tempo sempre foi.

## As fricções que a IA acabou de expor

Você conhece essas. Você viveu elas semana passada.

**A reunião que deveria ter sido uma spec.** Três calls de alinhamento para decidir o que construir. O modelo escreve em vinte minutos. Os vinte minutos nunca foram o problema, e nenhuma ferramenta acelera uma reunião.

**A única pessoa que sabe.** Metade do trabalho trava esperando o engenheiro que carrega o módulo de pagamentos na cabeça. O modelo lê o seu repositório. Ele não lê a memória de um colega, e essa memória é um ponto único de falha que você contorna há anos.

**O contrato que mora na cabeça de alguém.** A IA pergunta o formato da API. Ninguém aponta para um documento. Era "sabido". Então o trabalho espera uma conversa de corredor, igual a antes.

**O ticket vago.** "Melhorar o onboarding." O modelo resolve a ambiguidade no código, não na intenção, então ele entrega uma coisa confiante, rápida e errada, e você descobre o que realmente queria depois de três rodadas de retrabalho. Aponte velocidade para um alvo borrado e você chega ao lugar errado mais cedo.

E por trás de tudo isso, o código pronto na terça só entra na sexta, porque a cadeia de revisão nunca ficou mais rápida enquanto a escrita ficou.

## A boa notícia está enterrada na má

Isso não é uma adoção fracassada. É a medição mais honesta que a sua organização tem há anos.

A IA fez a parte que parecia cara de graça e te entregou um mapa preciso das suas restrições reais. A maioria dos times nunca recebe esse mapa. Eles continuam convencidos de que o gargalo é capacidade de engenharia, contratam mais engenheiros, e veem as reuniões, a espera e o retrabalho escalarem junto com o headcount. Agora você sabe melhor. O portão não é o código. Nunca foi.

## As soluções são chatas, e já funcionam

Nada disso precisa de uma ferramenta nova. Precisa da intenção escrita antes da reunião, para que a reunião encolha ou desapareça. Precisa do contexto commitado no repositório, para que a única pessoa que sabe deixe de ser gargalo e vire um arquivo que o modelo lê. Precisa da prioridade decidida uma vez, por escrito, para que o time entregue rápido numa direção em vez de rápido em cinco.

Eu já escrevi cada uma dessas. Que [contexto não é trabalho de dev](/pt-br/posts/2026-05-24-context-is-not-a-dev-job/) é a ideia que sustenta tudo: metade do que a IA precisa mora fora da engenharia, na cabeça de quem é dono do porquê. O [loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) é como a intenção é escrita antes do código. E [pagar o imposto de setup uma vez](/pt-br/posts/2026-06-15-commit-the-context/) é como o conhecimento tribal para de sair pela porta toda noite.

## Rode o teste na sua própria semana

Da próxima vez que algo demorar demais, não chute. Cronometre. Divida as horas em duas pilhas: horas em que a IA estava escrevendo código, e horas de todo o resto. O decidir, o esperar, o reexplicar, o aprovar.

Se codar foi a fatia fina, pare de pedir para o modelo ir mais rápido. Ele já foi. A próxima aceleração não é uma ferramenta que você compra para o time. É um processo que você tem que construir, e agora você sabe exatamente para onde apontá-lo.
