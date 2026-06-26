---
title: "O Treinamento Acaba Antes de Você Chegar"
subtitle: "O modelo nunca aprende com suas conversas. Ele chegou pronto. O que parece aprendizado dentro de uma sessão é contexto, e morre quando você fecha a aba."
date: 2026-06-25
description: "Corrija o modelo e ele se adapta, depois esquece até amanhã. Ele nunca aprendeu, ele releu. Os pesos congelam antes de o modelo sair, toda sessão começa do mesmo objeto congelado, e o aprendizado dentro da sessão é contexto, não treinamento. Fine-tuning versus contexto de uma vez."
cover: /assets/img/2026-06-25-training-is-over.png
coverAlt: "Uma galeria em carvão profundo onde uma única escultura acabada, iluminada em âmbar, está completa sobre um pedestal, com uma luz teal suave passando ao lado sem alterá-la, textura de pincelada e brilho suave."
---

Você diz ao modelo que ele errou. Você explica a regra. Ele concorda, e a partir dali segue a regra perfeitamente. Pelo resto da sessão ele guarda seu nome, suas preferências, a correção que você fez uma hora atrás. Parece que ele aprendeu.

Abra uma conversa nova amanhã e tudo sumiu. O nome, a regra, a correção. Em branco. Você não ensinou nada a ele. Ele releu o que estava na frente dele, e depois a página foi apagada.

## O modelo já está pronto

O treinamento aconteceu no passado. Antes de o modelo chegar até você, ele passou por um processo longo e caro. Ele leu uma quantidade enorme de texto e ajustou bilhões de números internos, seus pesos, até ficar bom em prever a próxima palavra. Aí o processo parou. Os pesos congelaram. O modelo saiu.

Toda conversa que você tem roda contra esse conjunto congelado de números. Assim como toda conversa de todo mundo. Você e um estranho do outro lado do mundo abrem o mesmo modelo, no mesmo estado, até a última casa decimal. Nada do que você faz numa conversa muda um único peso. O modelo que responde sua última mensagem é idêntico ao que respondeu a primeira.

## Então o que parecia aprendizado?

Contexto.

A correção que você deu não atualizou o modelo. Ela ficou na janela de contexto, o espaço de trabalho que o modelo relê do zero a cada turno. Enquanto suas palavras estão nessa janela, elas moldam o que vem em seguida. O modelo parece ter se adaptado porque está lendo sua correção toda vez que gera uma resposta. Limpe a janela, comece uma sessão nova, e suas palavras não estão mais lá para serem lidas. Não há nada para esquecer, porque nada nunca foi guardado. Escrevi sobre isso em [A Janela de Contexto É uma Mesa, Não uma Memória](/pt-br/posts/2026-06-10-context-window-desk-not-memory/).

É o truque inteiro. Aprendizado dentro da sessão não é aprendizado. É leitura.

## Dois jeitos de mudar o comportamento

Existem exatamente dois jeitos de fazer um modelo se comportar de forma diferente, e eles não têm o mesmo tamanho.

Um é o fine-tuning. Você pega o modelo congelado e roda mais treinamento nele, com novos exemplos, até os pesos mudarem. Isso é mudança real no próprio modelo. Também é lento, caro, feito offline por quem é dono dos pesos, e produz um novo modelo congelado, não um modelo ainda capaz de aprender. Fine-tuning é raro, e quase ninguém recorre a ele para resolver um problema do dia a dia.

O outro é o contexto. Você coloca instruções, exemplos e fatos na janela, e os pesos congelados existentes respondem a eles. Nada muda dentro do modelo. Você está dirigindo um objeto fixo com a entrada que entrega a ele. Isso é barato, instantâneo, por sessão, e é o que você faz toda vez que escreve um prompt, cola um guia de estilo ou corrige um erro.

Quase tudo que você imagina como fazer o modelo executar X é contexto, não treinamento. Quando você se sente tentado a dizer que ensinou algo ao modelo, você quase sempre quer dizer que colocou algo bom na janela.

## O que isso muda

Algumas coisas saem disso depois que você assimila.

O modelo é reproduzível. Os mesmos pesos para todo mundo significam que o comportamento que você obtém é função da entrada, não de algum histórico privado que o modelo construiu com você. Se duas pessoas recebem respostas diferentes, a diferença está no contexto, não no modelo.

Você instrui, você não implora. Sua frustração não treina o modelo, então repetir mais alto não faz nada. O que funciona é colocar a coisa certa na janela. Uma instrução clara vence uma terceira correção.

Recursos de memória são contexto salvo, não aprendizado. Quando uma ferramenta lembra de você entre sessões, ela está guardando texto em algum lugar e colando de volta na janela na próxima vez. Útil. Ainda é contexto. Os pesos nunca se moveram.

Sua correção não gruda sozinha. Como a correção vive só na janela, ela morre com a sessão. Se você quer ela toda vez, precisa colocá-la em algum lugar que é re-fornecido a cada execução: um system prompt, um arquivo de projeto, um [CLAUDE.md versionado](/pt-br/posts/2026-06-15-commit-the-context/). É a mesma razão pela qual argumentei que você deveria [capturar correções como regras duráveis](/pt-br/posts/2026-05-31-fix-the-system-not-the-output/) em vez de corrigir a mesma coisa duas vezes.

## Uma pergunta sobre a qual isto não é

As pessoas fazem uma pergunta relacionada: minha conversa é usada para treinar a próxima versão do modelo? É uma pergunta real com uma resposta real, e a resposta depende do provedor e das suas configurações. Também é uma pergunta diferente. É sobre uma rodada de treinamento futura da qual você não faz parte. Este post é sobre o modelo na sua frente agora, que está pronto e não vai mudar enquanto você o usa.

## Fechamento

O modelo não está crescendo junto com você. Ele chegou pronto. Toda sessão o inicia do mesmo estado congelado, lê o que você põe na frente dele e esquece tudo no instante em que você fecha a aba.

Então pare de tentar ensiná-lo. Você não é o professor dele, você é o instrutor de plantão. Toda sessão é o dia um, e a qualidade do dia depende de quão bem você o instrui.
