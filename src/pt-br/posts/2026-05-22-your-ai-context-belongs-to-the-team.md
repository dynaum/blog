---
title: "O Contexto da Sua IA Pertence ao Time"
subtitle: "Toda sessão com uma IA é uma sessão de ensino. A maioria dos times joga o ensino fora. Aqui está como guardá-lo, compartilhá-lo, e deixá-lo render juros."
date: 2026-05-22
description: "O contexto que você constrói com a IA em sessões privadas é um ativo do time. Como guardá-lo numa base de conhecimento compartilhada com o Obsidian, gerenciar a camada de CLAUDE.md no repositório, e tornar o AI-DLC mais fácil."
cover: /assets/img/2026-05-22-your-ai-context-belongs-to-the-team.png
coverAlt: "Uma constelação de pequenas notas âmbar brilhantes ligadas por fios finos de luz azul-esverdeada, como um grafo de conhecimento visto no escuro."
---

Toda vez que você abre uma sessão com uma IA, você a ensina. Você explica o formato da base de código, as convenções, as regras do domínio, a pegadinha do mês passado, a razão de um trecho estranho de código ser estranho. Esse ensino é trabalho de verdade. É também uma das coisas mais valiosas que você produz no dia, e a maioria dos times joga isso na lixeira no momento em que a sessão fecha.

Aqui está o padrão que eu sempre vejo. Um desenvolvedor passa vinte minutos colocando o modelo a par de um serviço. Ele faz um bom trabalho, a sessão termina, e o contexto vai embora junto. No dia seguinte um colega abre uma sessão nova e explica o mesmo serviço do zero. Os mesmos vinte minutos. A mesma explicação. Ninguém é preguiçoso e ninguém está errado, e mesmo assim o time paga o imposto todo dia. O taxímetro está rodando e ninguém vê.

A correção começa com um reenquadramento. O contexto de IA não é um artefato pessoal. É infraestrutura. A base de conhecimento que você constrói para o seu próprio modelo é, quase linha por linha, a base de conhecimento de que o desenvolvedor ao seu lado precisa. Trate-a como você trata código. Escreva uma vez, coloque num lugar compartilhado, versione, e deixe todo mundo usar.

A ferramenta para a qual eu apelo é o [Obsidian](https://obsidian.md/). A razão é estreita e importa. Um cofre do Obsidian é uma pasta simples de arquivos Markdown. Você o lê por uma interface limpa, com links e uma visão em grafo. Um agente de IA lê os mesmos arquivos diretamente, sem exportação e sem conversão. A base de conhecimento que o seu time mantém e a base de conhecimento que o modelo consome são uma coisa só, não duas cópias se distanciando.

O resto é elenco de apoio. As notas se ligam umas às outras, então uma nota sobre um sistema aponta para o princípio por trás dele. O cofre é uma pasta git, então a base de conhecimento versiona junto com o trabalho. E nada disso está preso ao Obsidian. Qualquer pasta de Markdown dá conta. O Obsidian é um bom padrão, não a única porta.

Uma estrutura em que confio: uma pasta de princípios para as regras duradouras, as notas de como-pensamos, e uma pasta por sistema ou domínio para as especificidades. Mantenha cada nota pequena e sobre uma coisa só. Ligue-as.

Eu faço isso para os meus jogos. Mantenho um cofre onde as lições de design de um jogo ficam numa pasta de princípios, separada da pasta do jogo em si. Quando começo o próximo jogo, não começo do nada. O modelo e eu abrimos o mesmo cofre, e as lições suadas do último projeto já estão na mesa. O primeiro jogo paga a mensalidade. Todo jogo depois dele lê as anotações. A ideia funciona na escala de uma pessoa entre projetos do mesmo jeito que funciona para um time entre pessoas.

O que vai nela? As pegadinhas, o porquê por trás das decisões, o vocabulário do domínio, as restrições não óbvias, os becos sem saída por onde você já passou. Um teste simples: se você explicaria para um recém-contratado na primeira semana dele, e também explicaria para uma sessão nova de IA, aquilo pertence à base compartilhada. Recém-contratados e sessões novas precisam das mesmas coisas.

Existe uma segunda camada, mais perto do código. Um arquivo `CLAUDE.md` ou `AGENTS.md` fica no repositório e carrega o contexto específico daquele projeto. O cofre guarda o conhecimento duradouro, entre projetos. O arquivo do repositório guarda o que só esta base de código precisa.

Gerenciar os dois é um hábito, não um processo. Quando você se pegar explicando ao modelo algo que já explicou antes, pare e escreva. Se for específico do projeto, vai no arquivo do repositório. Se for um princípio duradouro, vai no cofre. Reexplicar a mesma coisa é o sinal. A segunda vez é um bug, e a correção é um parágrafo. Faça a poda da mesma forma. Um arquivo de contexto desatualizado custa mais do que um vazio, então apague o que não é mais verdade.

Isso rende direto se o seu time está caminhando para o AI-DLC. O AI-DLC roda sobre steering files, arquivos de regras compartilhados que restringem o agente. Um time com uma base de contexto compartilhada de verdade já é dono da matéria-prima. Os steering files viram um trabalho de curadoria, não uma página em branco. O [post anterior](/pt-br/posts/2026-05-21-you-cannot-push-a-developer/) neste blog argumentou que o atrito é o que trava a adoção. Uma base de contexto fina ou inexistente é atrito. Uma boa o remove.

O [loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) mantém um modelo nos trilhos escrevendo o contexto. Este é o mesmo movimento, no plural. O contexto que você escreve hoje são os vinte minutos que um colega não perde amanhã, e a vantagem que o seu próximo projeto ganha de graça. Pare de acumular. Coloque num lugar onde todo mundo, e toda sessão, vão encontrar.
