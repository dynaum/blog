---
title: "Não Apenas Use o Modelo"
subtitle: "A série diz que o desenvolvedor é dono das decisões. Mas uma decisão sobre uma máquina que você trata como mágica é um chute. Três escolhas reais que vieram de saber como o modelo funciona, e três livros acessíveis para te levar lá."
date: 2026-05-30
description: "A qualidade de toda decisão sobre um sistema de IA é limitada por quão bem você entende a máquina. Três escolhas reais (RAG vs fine-tuning, projetar em torno da alucinação, quando não usar um LLM) e três livros acessíveis para chegar lá."
cover: /assets/img/2026-05-30-dont-just-use-the-model.png
coverAlt: "Uma máquina aberta sobre uma bancada escura à noite, sua carcaça erguida revelando engrenagens internas intrincadas brilhando em âmbar quente por dentro, uma luz de contorno azul-petróleo traçando as bordas de metal."
---

Já vi mais de um time tentar ensinar a um modelo o próprio produto fazendo fine-tuning. Semanas de trabalho. Um dataset, um treino, uma conta para pagar. Aí eles perguntam algo sobre a própria documentação e ele inventa uma resposta com total confiança. O modelo nunca foi o problema. Ninguém tinha perguntado o que o fine-tuning de fato muda.

Este blog disse a mesma coisa em todo post. O desenvolvedor é dono da intenção e do julgamento. O modelo é dono da estrutura e da execução. Há uma precondição escondida nessa frase. Seu julgamento sobre um sistema de IA é tão bom quanto seu entendimento de como o sistema funciona. Uma decisão sobre uma máquina que você trata como mágica é um chute com cara de confiança.

Um usuário dirige o modelo. Quem constrói sabe por que ele se comporta. A diferença entre os dois não é habilidade de prompt. É saber o que a máquina está fazendo quando responde. Esse conhecimento é o que te diz quando confiar nela, o que construir ao redor dela, e quando não recorrer a ela.

## Três decisões que vieram de conhecer a máquina

**RAG ou fine-tuning.** Treinar grava padrões nos pesos. Não constrói um repositório de fatos em que você possa confiar. O fine-tuning muda comportamento, tom e formato. Não ensina de forma confiável os seus dados atuais ao modelo. Então a pergunta se responde sozinha quando você conhece o mecanismo. "Responder a partir da nossa documentação, com fatos atuais" é um problema de retrieval. Injete os fatos na inferência com RAG. "Seguir a nossa voz, devolver o nosso formato de saída" é um problema de fine-tuning. O time que faz fine-tuning para injetar conhecimento queima semanas e ainda recebe respostas inventadas, porque o conhecimento foi parar onde nunca ia morar. Saber a diferença entre treino e inferência é a decisão inteira, e é uma semana economizada já na primeira manhã.

**Alucinação é estrutural.** Um modelo de linguagem amostra o próximo token de uma distribuição de probabilidade. Ele sempre produz texto fluente. Não tem um "eu não sei" interno, porque confiança não é um valor que ele calcula. Quando você sabe disso, para de pedir ao modelo para ser preciso e passa a projetar a precisão. Aterre com retrieval. Verifique a saída antes de ela subir. Coloque um portão humano em qualquer coisa com consequências. Este é o argumento do [Confie no Pipeline](/pt-br/posts/2026-05-23-trust-the-pipeline/) movido uma camada abaixo. Trabalho num domínio regulado onde código errado tem consequências, e ali a camada de verificação não é um luxo. Ela decorre diretamente de entender o que o modelo é. Nunca decorre de torcer para o modelo se comportar.

**Às vezes a resposta não é um modelo.** A área é mais antiga e mais ampla do que os foundation models de que todo mundo fala. Um problema determinístico quer uma ferramenta determinística. Um solver de restrições, um motor de regras, uma simples query no banco. Uma classificação de alto volume quer um modelo pequeno e rápido, com o grande reservado para o passo de raciocínio difícil. Recorra ao maior modelo em todo problema e você paga em latência, em custo, e em instabilidade que não consegue explicar. Conhecer o mapa mais amplo da área é o que te deixa escolher a ferramenta certa em vez da famosa.

## Por onde começar

Nada disso exige um PhD. Exige alguns livros e a disposição de lê-los. Aqui estão os três que eu indico, do mais fácil primeiro.

**[Artificial Intelligence: A Guide for Thinking Humans](https://www.amazon.com/dp/1250758041/ref=nosim?tag=dynaum21-20)** de Melanie Mitchell. O panorama geral, em linguagem simples. O que IA é, o que não é, e por que a história de que "o modelo entende" é a armadilha por trás de metade das decisões ruins acima. Sem matemática. Leia este e a armadilha da confiança para de te enganar.

**[Deep Learning](https://www.amazon.com/dp/0262537559/ref=nosim?tag=dynaum21-20)** de John D. Kelleher, na série MIT Press Essential Knowledge. Os mecanismos, de forma curta. Como uma rede aprende, o que o treino guarda e o que não guarda, por que um modelo generaliza e por que ele confabula. Um livro pequeno com um grande retorno. Leia este e as duas primeiras decisões deixam de ser um mistério.

**[AI Engineering](https://www.amazon.com/dp/1098166302/ref=nosim?tag=dynaum21-20)** de Chip Huyen. A camada aplicada. RAG, avaliação, custo de inferência, quando o fine-tuning vale a pena. As decisões que você toma construindo sistemas reais sobre foundation models. Leia este e o entendimento vira as escolhas que você faz no trabalho.

Leia em qualquer ordem. Mitchell para o panorama, Kelleher para o mecanismo, Huyen para a construção. Comece pelo topo e desça, ou comece pelo Huyen, onde seu trabalho já está, e desça uma camada quando uma decisão precisar.

## O que isto não é

- Não é uma regra de que você precisa ler os três antes de ter permissão para construir. Um livro é mais do que nenhum.
- Não é um chamado para virar pesquisador. O argumento é qualidade de decisão na camada de aplicação, não uma mudança de carreira para treinar modelos.
- Não é um voto contra abstração. Você não precisa saber como um compilador funciona para escrever a maior parte do código. Mas quanto mais decisões você é dono num sistema, menos os internos dele continuam opcionais.

## Fechamento

Posts anteriores construíram fundações para usar IA bem. Specs para o modelo não se perder. Contexto compartilhado para o time parar de re-explicar. Observabilidade para o agente ler algo verdadeiro. Esta é a fundação debaixo dessas fundações. Cada uma delas é uma decisão, e uma decisão sobre uma máquina é tão boa quanto a sua imagem da máquina.

Um usuário recebe saída. Quem constrói decide se a saída deve ser confiada, e como construir o sistema para que a resposta seja sim. Não apenas use o modelo. Aprenda o que ele está fazendo quando responde. É daí que vêm as boas decisões.

---

*Os links da Amazon acima são links de afiliado. Se você comprar por um deles, eu recebo uma pequena comissão, sem custo extra para você. Só recomendo livros que eu mesmo estou lendo.*
