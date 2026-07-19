---
title: "Como o Dia Realmente Funciona"
subtitle: "Um dia real construindo e operando software com IA: personas de usuário predefinidas apontam cada agente para a pessoa mais difícil, agentes em paralelo dentro de worktrees fazem a construção, e loops percorrem a produção a noite toda como essas mesmas personas."
date: 2026-07-18
description: "Uma recomendação no formato dia a dia. Personas de usuário escritas como regras apontam cada agente para o usuário mais difícil, worktrees deixam agentes paralelos construírem sem colidir, e loops mais goals sustentam a produção percorrendo os fluxos críticos como essas personas. Uma ideia conecta tudo: escreva a pessoa uma vez, reutilize em todo lugar."
cover: /assets/img/2026-07-18-how-the-day-runs.png
coverAlt: "Uma bancada escura vista de cima à noite com várias pequenas estações de trabalho iluminadas ativas ao mesmo tempo, um marcador de figura diferente em cada uma representando uma persona de usuário, e uma luminária âmbar quente deixada acesa sobre um pequeno monitor mostrando uma linha de batimento cardíaco, luz de contorno azul-esverdeada, textura de pincelada e brilho suave."
---

Uma paciente idosa abriu o app, tocou no botão de enviar duas vezes porque o primeiro toque não deu retorno nenhum, e não mandou nada. A tela parecia pronta para mim. Não estava pronta para ela. Eu nunca teria percebido, porque eu não sou ela. Meus polegares são rápidos, meus olhos são bons, e eu já sei o que o botão faz.

Então parei de construir para mim. É assim que um dia normal funciona agora.

## Manhã: eu construo para uma pessoa, escrita

Eu não peço para um agente "construir o formulário de cadastro". Eu entrego a ele uma pessoa. A paciente. A usuária idosa com zero conhecimento de tecnologia e a tela do celular rachada. O administrador processando um lote de duzentos registros antes do almoço. Cada um é uma regra escrita: o que sabem, o que temem, o dispositivo na mão, a coisa que faz desistirem e ligarem para o suporte.

Com a persona idosa, o agente percebe o toque duplo sem retorno. Com a persona da paciente, ele sinaliza o botão de baixo contraste e a mensagem de erro que parece um stack trace. Com a persona do administrador, ele nota que a tela de lote não tem como desfazer uma única linha errada entre duzentas.

A regra é o ponto inteiro. Uma persona que você guarda na cabeça é um estereótipo que você aplica quando lembra. Uma persona escrita é uma lente que todo agente usa toda vez, esteja eu olhando ou não. É o mesmo movimento de [commitar o seu contexto](/pt-br/posts/2026-06-15-commit-the-context/): escreva uma vez, e o repositório entrega ao modelo em cada sessão em vez de você reexplicar o usuário para sempre.

## Meio-dia: mais de um agente exige worktrees

No fim da manhã eu estou rodando três agentes, e no momento em que há mais de um, eu viro o gargalo e o sistema de arquivos vira a primeira baixa. Dois agentes editando o mesmo checkout colidem. Um reformata um arquivo que o outro está no meio de editar. Os branches se embolam.

Um worktree resolve isso na raiz. Cada agente ganha sua própria cópia do repositório no seu próprio branch, seu próprio diretório de trabalho, seu próprio espaço para errar. Agora um agente constrói a tela de lote do administrador enquanto outro percorre o fluxo da paciente de ponta a ponta, ao mesmo tempo, e nenhum toca nos arquivos do outro. Esse é o requisito que torna os agentes paralelos reais, não um luxo. Rode dois agentes num diretório só e você vai passar a tarde desembolando em vez de entregando. Aprendi o [problema dos múltiplos agentes](/pt-br/posts/2026-05-27-many-agents-one-chat/) do jeito lento. O worktree é a parte que torna isso seguro.

As personas viajam para dentro de cada worktree. Os mesmos arquivos de regra carregam em cada cópia, então a paciente é a mesma paciente esteja um agente construindo a feature, revisando o diff, ou checando em produção. Escrevi a pessoa uma vez. Todo agente, em todo lugar, lê a mesma.

## Segundo plano: loops sustentam a produção a noite toda

A parte que um dia de agente único nunca tem: trabalho que roda enquanto eu durmo. Um loop é uma vigília constante, e os meus não vigiam de forma abstrata. Eles vigiam como a persona.

Um loop percorre o fluxo crítico, o login e a única tarefa que paga as contas, como a usuária idosa de pouca tecnologia. Ele toca devagar, lê errado, hesita, e quando o fluxo quebra ou fica confuso ele abre uma issue antes de uma pessoa real bater nela. Um segundo loop varre dependências e código atrás de vulnerabilidades conhecidas e registra um relatório no instante em que algo entra numa lista de CVE. Uma terceira peça não é um loop. Quando uma quebra é sinalizada, eu a entrego a um goal: conserte isso, e a condição só fecha quando o fluxo passa de novo e um modelo novo confirma.

Essa separação importa, e eu [já escrevi sobre ela](/pt-br/posts/2026-07-07-wake-up-and-done/). Um loop é dono do relógio, ele volta numa cadência e vigia o mundo lá fora. Um goal é dono da linha de chegada, julgada por um segundo modelo que não escreveu a correção. Um loop é bom em notar. É ruim em decidir que terminou. Então o loop nota o fluxo quebrado da paciente, e o goal leva a correção a um fechamento verificado. Vigiar e consertar são trabalhos diferentes, e dar a cada um sua própria ferramenta é por que a cobertura se sustenta.

## Por que isso funciona, e não é o modelo

Nada disso é porque o modelo ficou mais esperto neste trimestre. O dia é coberto porque o trabalho é apontado.

As personas fazem o software ser sobre a pessoa certa, a mais difícil em vez da média imaginária. Os worktrees tornam três agentes seguros em vez de um desastre de merge. Os loops tornam a cobertura constante em vez de uma coisa que eu lembro de checar nas sextas. Mira vence potência. Um modelo de ponta apontado para o usuário errado constrói uma coisa linda que ninguém consegue usar. Um modelo mais barato apontado para a paciente, rodando num worktree isolado, vigiado por um loop que percorre o fluxo dela às 3 da manhã, entrega algo que funciona para ela.

## Monte nesta ordem

Não construa o dia inteiro de uma vez. Adicione uma restrição por vez.

Escreva o arquivo de regra de uma persona hoje, e que seja o seu usuário mais difícil, não o mais fácil. A pessoa que não enxerga bem, não toca com precisão, ou nunca usou um software como o seu. Adicione um worktree na primeira vez que você se pegar rodando dois agentes num diretório só. Aponte um loop para o seu fluxo de produção mais importante nesta semana, e faça ele percorrer esse fluxo como essa persona.

Cada peça se paga sozinha. Juntas, elas viram um dia que roda sozinho entre as suas decisões, e cada parte dele está olhando para a pessoa que de fato usa o que você entrega.
