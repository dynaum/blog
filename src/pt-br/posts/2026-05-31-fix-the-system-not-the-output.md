---
title: "Conserte o Sistema, Não a Saída"
subtitle: "Corrigir o que a IA produziu resolve hoje. Corrigir como ela funciona resolve todos os amanhãs. Reexplicar contexto não é só lento, deixa o objetivo desviar. Capture a decisão uma vez."
date: 2026-05-31
description: "Quando uma IA erra, corrigir a saída resolve um caso e corrigir o sistema resolve todos os futuros. Por que reexplicar contexto desvia o objetivo, e os três lugares para uma decisão capturada: uma skill, uma memória, um arquivo de projeto."
cover: /assets/img/2026-05-31-fix-the-system-not-the-output.png
coverAlt: "Um único formão cortando um sulco fundo e limpo na pedra escura, o corte brilhando em âmbar quente por dentro, com leves arranhões rasos e repetidos ao lado, em ciano mais frio, que não pegaram."
---

Me peguei digitando a mesma correção pela terceira vez. A mesma nota para o modelo, o mesmo conserto para o mesmo tipo de erro, em outro dia. A terceira vez é a que dói, porque a essa altura não é o modelo se repetindo. Sou eu.

Há duas formas de responder quando uma IA erra. Você pode consertar a saída. Você pode consertar o sistema.

Consertar a saída é editar o artefato até ele ficar certo. O pull request está correto, o documento lê bem, o bug sumiu. Você sobe. A coisa que produziu aquilo está exatamente como estava, então na semana que vem o mesmo erro chega e você faz a mesma correção de novo. Consertar o sistema é transformar essa correção numa regra que o modelo lê antes de agir, para que o erro não possa acontecer uma segunda vez.

A maioria de nós conserta a saída toda vez. Parece produtivo. No momento, é o movimento mais rápido. Ao longo do mês, é o mais lento, porque você paga o custo em cada repetição, e as repetições não param sozinhas.

## Repetição é desvio, não só atraso

A reclamação de sempre sobre reexplicar contexto é que desperdiça tempo. O custo mais profundo é a correção.

Toda vez que você explica algo de novo, você formula um pouco diferente. O modelo não vê a sua intenção. Ele vê as palavras que recebeu desta vez, e constrói para essas palavras. Duas explicações um pouco diferentes produzem dois resultados um pouco diferentes. O objetivo desvia um grau a cada repetição, e você não percebe até a saída estar a alguns graus de onde você começou, sem conseguir apontar o momento em que entortou.

Uma decisão escrita remove a variância. Uma fonte da verdade, formulada uma vez, lida do mesmo jeito por toda sessão. Este é o loop guiado por spec apontado para uma parte mais tardia do ciclo. A [spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) existe para a intenção não mutar entre a ideia e o código. A decisão capturada existe para a intenção não mutar entre a correção e a próxima vez que o trabalho voltar.

## O comprovante

Esta semana, neste blog. Eu publico um post da mesma forma toda vez. Spec, rascunho, capa, tradução, verificação, envio. Por um bom tempo eu reexplicava esse fluxo para uma sessão nova em cada post. Aí parei de consertar a saída e consertei o sistema. O fluxo agora é uma skill. O modelo a carrega quando começo um post, e eu não narro mais os passos.

Um mais afiado. Gerar a imagem de capa falhava sempre do mesmo jeito, uma página de erro baixada e salva como se fosse uma figura. Consertei essa saída mais de uma vez antes de transformar em regra. Agora é uma linha que o modelo segue, e a falha sumiu.

A parte honesta. No início da mesma semana eu reconstruí uma peça de ferramenta que já existia, porque eu nunca tinha escrito onde ela morava. Reexpliquei o objetivo, o modelo construiu algo novo, e duplicou um trabalho que já estava no repositório. A lição me mordeu antes de eu terminar de escrevê-la. É o argumento inteiro num só hematoma. A segunda vez é um bug, e fui eu quem subiu esse bug.

## Onde a decisão mora

Depois que você decide capturar uma correção, ela precisa de um lar. São três, e a escolha é sobre escopo, não gosto.

Uma **skill**, para um procedimento repetido. Quando a coisa que você fica reexplicando é como fazer algo, escreva como uma instrução que o modelo executa, não um parágrafo que ele talvez leia. Executável vence passivo. Um documento pode ser ignorado. Uma skill é o passo.

Uma **memória ou nota no vault**, para uma decisão durável que sobrevive a um projeto. A preferência, a razão por trás de uma escolha passada, o beco sem saída que você já percorreu para não percorrer de novo. Conhecimento entre projetos pertence a algum lugar que todo projeto alcança, não enterrado num repositório.

Um **arquivo CLAUDE.md ou AGENTS.md**, para contexto específico do projeto. As convenções, as armadilhas, as regras que só este código precisa. Ele carrega toda sessão, então o modelo começa informado em vez de adivinhar e desviar.

Os nomes são meus e as ferramentas vão mudar. As formas não. Todo setup de agente tem as mesmas três: um procedimento, um fato durável, uma regra de projeto. Coloque a decisão na que combina com o escopo dela, e ela deixa de ser algo que você fala e passa a ser algo que o sistema sabe.

## O que isto não é

- Não é "documentar tudo". Uma wiki que ninguém lê é o modo de falha, não a meta. Capture regras duráveis, e pode as que ficam obsoletas. Uma regra obsoleta custa mais que uma ausente, porque mente com autoridade.
- Não é "nunca corrija a saída". Você ainda conserta o artefato na sua frente. Aí você faz uma pergunta. Vou consertar isto de novo? Se a resposta é sim, você promove.
- Não é automatizar o julgamento. Decidir o que vale capturar é o seu trabalho. O modelo não distingue um caso único de uma regra. Você distingue.

## Fechamento

O trabalho nunca foi a correção. Qualquer um conserta a saída, e o modelo aceita o conserto de bom grado e o esquece na sessão seguinte. O trabalho é fazer a correção uma vez, num lugar que segura, para que a próxima sessão comece onde esta terminou, e não onde as dez últimas começaram.

Conserte a saída e você tem um artefato melhor. Conserte o sistema e você tem um sistema melhor. Só um dos dois compõe.
