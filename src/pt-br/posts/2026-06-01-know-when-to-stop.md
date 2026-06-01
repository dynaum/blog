---
title: "Saiba a Hora de Parar"
subtitle: "A habilidade que separa um sênior de um júnior afobado é saber quando o modelo é a ferramenta errada. Estar disponível não é servir. Quatro momentos para largar o prompt."
date: 2026-06-01
description: "Um contrapeso a uma série pró-IA: saber quando não recorrer ao modelo é uma habilidade de sênior. Quatro casos em que a IA custa mais do que economiza, tratados como julgamento, não ceticismo."
cover: /assets/img/2026-06-01-know-when-to-stop.png
coverAlt: "Uma bancada à noite, uma mão pousada sobre uma chave de fenda simples sob luz âmbar quente, enquanto uma máquina maior e mais elaborada está desligada e fria na sombra azul-petróleo ao lado."
---

Perdi uma hora na semana passada para uma tarefa que o modelo não tinha o que fazer tocando. Um pequeno arquivo de dados precisava ser remodelado. O modelo estava ali, então eu fiz o prompt. A saída ficou perto. Corrigi. Mais perto. Corrigi de novo. Uma hora depois, eu tinha um resultado que ainda precisava ler linha por linha para confiar. Um script de cinco linhas teria feito em dez minutos, correto por construção, sem revisão.

O modelo não falhou. Eu falhei. Recorri a ele porque estava disponível, e disponível não é o mesmo que servir.

Este blog passou catorze posts sobre usar IA bem. Este é o contrapeso, e eu ganhei o direito de escrevê-lo. Saber a hora de parar é a habilidade que separa um sênior de um júnior afobado. O júnior recorre ao modelo toda vez, porque ele está ali e é rápido. O sênior sabe, antes da hora ir embora, que esta é uma das vezes de largar o prompt.

## Quatro momentos para parar

**Quando a revisão custa mais do que o trabalho economizado.** O modelo produz quase qualquer mudança pequena em segundos. Você ainda tem que ler cada linha para confiar, e abaixo de certo tamanho essa leitura é mais lenta do que só digitar o conserto. Uma edição de três linhas que você entende de cor não é trabalho para um prompt. O modelo desloca seu trabalho de escrever para revisar, e para mudanças pequenas e óbvias, escrever era a metade mais barata.

**Quando a resposta precisa ser exata e você não consegue verificar barato.** Um regex que você vai olhar e aprovar errado. Uma regra de arredondamento financeiro. Uma condição de borda em que uma resposta plausível-mas-errada é cara. O modelo produz uma saída fluente e confiante, sem nenhum sinal da própria dúvida. Se checar a resposta é tão difícil quanto produzi-la, o modelo não economizou nada e te entregou um risco. Trabalho num domínio regulado onde código errado tem consequências, e ali uma resposta confiante e errada é pior do que nenhuma resposta.

**Quando o problema é determinístico.** Um rename em uma dúzia de arquivos. Uma query estruturada. Uma conversão de formato. Um codemod. Essas coisas têm ferramentas exatas que são corretas por construção, toda vez. Pedir a um modelo probabilístico para fazer o que uma ferramenta determinística faz perfeitamente é trocar uma garantia por um chute. Use o rename. Rode a query. A ferramenta chata é a ferramenta certa.

**Quando você não consegue assumir a saída.** Se você não entende o resultado bem o suficiente para revisá-lo, você não pode subi-lo, e colar mesmo assim é como código que ninguém entende entra na base. Pare antes de colar. Ou aprenda o bastante para assumi-lo, ou não o use. Esta é a regra do operador-no-loop do [post de operação](/pt-br/posts/2026-05-26-save-the-boring-time/), apontada para o seu próprio teclado. O modelo propõe. Você decide. Você não pode decidir sobre algo que não consegue ler.

## O comprovante

O arquivo de dados foi um. Aqui está o que dói mais. Na semana anterior, pedi ao modelo para construir uma peça de ferramenta, e ele construiu algo novo e razoável. O problema é que a ferramenta já existia no repositório. Eu tinha recorrido ao modelo para construir antes de olhar o que já estava lá. Paguei por uma coisa que eu já tinha.

As duas falhas são o mesmo erro. O modelo foi a primeira coisa que agarrei, não a coisa certa. O custo não foi um bug nem uma saída ruim. O custo foi a hora, e a hora não volta.

## O que isto não é

- Não é anti-IA. Os catorze posts antes deste continuam de pé. Para a maior parte do trabalho, o modelo ainda é a ferramenta certa, e recorrer a ele ainda é o instinto certo. Este é o limite desse instinto, dito com honestidade.
- Não é uma regra que você aplica mecanicamente. Não há contagem de linhas, nem checklist, nem nota. É julgamento, e julgamento é a parte que continua sua.
- Não é desculpa para fugir da ferramenta. "Eu faço na mão" pode ser a própria preguiça, a fuga de aprender uma coisa que renderia por meses. Parar é certo quando o modelo é o encaixe errado, não quando você está fugindo da rampa de entrada.

## Fechamento

A série sempre dividiu o trabalho do mesmo jeito. O modelo é dono da execução. Você é dono do julgamento. O primeiro julgamento, antes de todo o resto, é se o modelo deveria tocar nesta tarefa. Essa decisão acontece nos primeiros dez segundos, e errá-la custa os próximos sessenta minutos.

Recorrer ao modelo é fácil, porque ele está sempre ali. Saber quando não recorrer é a habilidade mais difícil, e a que vale construir.
