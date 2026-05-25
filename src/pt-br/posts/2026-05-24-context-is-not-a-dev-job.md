---
title: "Contexto Não É Coisa de Dev"
subtitle: "Metade do contexto que uma IA precisa mora na cabeça das pessoas fora da engenharia que são donas da intenção. O AI-DLC só funciona quando essa metade é escrita, no mesmo cofre e no mesmo template de spec que os engenheiros usam."
date: 2026-05-24
description: "O contexto compartilhado de IA era metade da fundação. A outra metade é produto, design, e as pessoas que são donas da intenção: usuário, problema, critérios de sucesso, não-objetivos, restrições, porquê. O AI-DLC só funciona quando as duas metades são escritas."
cover: /assets/img/2026-05-24-context-is-not-a-dev-job.png
coverAlt: "Um caderno aberto sobre uma mesa de madeira escura à noite, com as duas páginas pegando o brilho quente de uma única lanterna âmbar entre elas. Um trabalho compartilhado, duas páginas, uma luz."
---

O post da semana passada defendeu o contexto de IA compartilhado. Era metade do post. A metade que deixei de fora é a mais cara.

Tudo naquele post era contexto de engenharia. O formato da base de código, as convenções, as pegadinhas, a convenção de testid. Uma fundação de verdade tem outra metade: o usuário, o problema, o porquê, os critérios de sucesso, as coisas que a funcionalidade não está tentando fazer. Essa metade mora na cabeça das pessoas fora da engenharia que são donas da intenção. Product managers, designers, analistas de negócio, dependendo da organização. Elas sempre foram donas disso. O AI-DLC traz uma exigência nova: escrever onde o agente consegue ler.

A maioria dos times pula essa metade. O cofre de engenharia cresce. A metade de produto fica em reuniões, briefings, threads e na cabeça das pessoas. O agente recebe um contexto técnico limpo e um contexto de intenção fino ou inexistente. Ele executa contra o melhor palpite do engenheiro sobre o que o briefing queria dizer. Uma semana depois a demo aterrissa e quem escreveu o briefing diz "não era isso que eu quis dizer." A decepção clássica, agora mais rápida.

Eu trabalho num domínio regulado onde código errado tem consequências. Intenção errada subindo mais rápido é pior do que intenção errada subindo devagar. A metade de produto do contexto é o que impede o agente de executar um mal-entendido em escala.

**O que a metade de produto contém.**

Uma lista curta, com o mesmo formato de uma spec de engenharia:

- **O usuário.** Para quem é isto, em uma frase, sem linguagem de marketing.
- **O problema.** Qual dor estamos removendo, nas palavras dela.
- **Os critérios de sucesso.** O que precisa ser verdade para a funcionalidade contar como pronta. Mensurável quando possível.
- **Os não-objetivos.** As coisas que isto não está tentando fazer. Mesma disciplina de uma spec de engenharia, talvez mais importante do lado de produto, porque é em produto que o escopo começa a inflar.
- **As restrições que não podem se mover.** Regulatórias, contratuais, de marca. As coisas que o agente não deve violar mesmo quando seria mais fácil.
- **O registro de decisões.** Por que esta abordagem em vez da rejeitada. Mesmo padrão de opção-rejeitada que engenharia usa, aplicado a trade-offs de produto.

Os engenheiros já escrevem parte disso para specs técnicas. Produto escreve no nível de produto. A estrutura do cofre fica a mesma: uma pasta de princípios para as regras duradouras, uma pasta por sistema ou domínio para as especificidades. A pasta de princípios ganha princípios de produto ao lado dos de engenharia. As pastas por sistema ganham notas técnicas e notas de produto. Um cofre, dois autores.

**Escrevendo para o agente.**

A menor ilustração possível e a mais útil. "Deixa o onboarding intuitivo" é o briefing que um PM entrega para um engenheiro. O engenheiro preenche a lacuna com o próprio gosto. Bons engenheiros preenchem bem. O agente preenche com o padrão mais comum nos dados de treino dele. Isso quase nunca é o que o briefing queria dizer.

O mesmo briefing, escrito para o agente:

- Um novo usuário chega ao primeiro estado útil em até dois cliques a partir de qualquer página.
- O primeiro estado útil é o dashboard com os primeiros dados dele já preenchidos, não um estado vazio.
- Passos exigidos do cadastro até o primeiro estado útil: conta, nome, um projeto. Qualquer coisa além disso é não-objetivo para o v1.

O agente consegue agir no segundo. Não consegue agir no primeiro. Cada adjetivo que o briefing teria deixado para o julgamento do engenheiro agora é um lugar onde o agente vai inventar alguma coisa. Escreva o critério ou aceite o que ele inventar.

Não há pergunta de acompanhamento. O agente não pausa para esclarecer. Ele roda contra o briefing que tem, agora mesmo, enquanto quem escreveu está em outra reunião. Input explícito é o que faz o async funcionar.

**Reenquadramento.**

Isso é mais do trabalho real de quem escreve o briefing, não mais do trabalho do engenheiro empurrado para cima dele. "Seja explícito sobre a intenção" sempre foi o trabalho. O novo colaborador apenas sobe o sarrafo do que "explícito" precisa significar.

Quem escreve intenção melhor recebe software melhor, mais rápido. O loop de feedback aperta. Essa é a vitória que importa para essas pessoas. É também o mesmo loop que o [post do loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) descreveu, com a metade de produto da spec escrita pela pessoa mais próxima da resposta.

**As mesmas cinco razões, do outro lado.**

Se você leu [o post sobre adoção de AI-DLC](/pt-br/posts/2026-05-21-you-cannot-push-a-developer/), as cinco razões pelas quais desenvolvedores resistem a uma metodologia nova têm um espelho do lado de produto. Já se queimaram com modismos de processo. O número de 10 a 15 vezes soa como marketing. O loop atual de briefing-e-reunião já entrega funcionalidades. A saída do agente ainda precisa ser revisada, o que parece trabalho saindo de briefing e indo para revisão. E veio da engenharia, o que invade o ofício de produto vindo de fora.

A mesma resposta usada com engenheiros. Mostre numa funcionalidade real. Mate a primeira semana de atrito. Faça do caminho padrão o bom caminho. Deixe os pares converterem os pares. Aceite um ritmo desigual.

A última razão é a mais difícil. Pedir que as pessoas donas da intenção escrevam dentro do template da engenharia pode parecer invasão de ofício. O reenquadramento de "isto é o seu ofício, mais afiado, não um processo da engenharia imposto a você" precisa vir de alguém com credibilidade dos dois lados. Senão, aterrissa como tomada de espaço.

Você também não empurra um PM.

**O padrão que funciona.**

Uma pessoa fora da engenharia que esteja disposta. Uma funcionalidade real, não um exemplo de brincadeira. O próximo ticket dela, o que ela teria feito briefing verbal.

Ela escreve o briefing dentro do mesmo template de spec que os engenheiros usam. Um engenheiro pareia com ela no primeiro rascunho. O trabalho do engenheiro no pareamento é fazer as perguntas que o agente teria de chutar e escrever as respostas. O PM internaliza as perguntas para a próxima vez. O engenheiro e o agente então constroem em cima do briefing. Demo.

Ela vê as palavras dela moldando a saída. Esse é o momento que traz a próxima pessoa.

O [post anterior](/pt-br/posts/2026-05-22-your-ai-context-belongs-to-the-team/) disse que o contexto da sua IA pertence ao time. O time é maior do que a engenharia. Uma fundação precisa das duas metades. A metade que você pula é a metade na qual o agente vai chutar, e o agente chuta em escala.

O que os engenheiros escrevem impede o modelo de se perder. O que produto escreve diz para onde ele deve andar.
