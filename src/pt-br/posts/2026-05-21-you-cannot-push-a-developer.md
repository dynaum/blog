---
title: "Você Não Empurra um Desenvolvedor"
subtitle: "Adotar o AWS AI-DLC numa organização de engenharia me ensinou que o verbo estava errado. Você não empurra as pessoas para uma metodologia. Você remove os motivos para dizer não."
date: 2026-05-21
description: "Notas de campo sobre conduzir a adoção do AWS AI-DLC: as cinco razões legítimas pelas quais bons desenvolvedores resistem a uma metodologia imposta, e o que de fato muda opiniões."
cover: /assets/img/2026-05-21-you-cannot-push-a-developer.png
coverAlt: "Um escritório aberto e escuro à noite, pequenas lanternas espalhadas pelas mesas, algumas acesas em âmbar quente e outras ainda apagadas."
---

Há alguns meses eu sou a pessoa na sala defendendo um jeito novo de construir software. Tenho uma metodologia em que acredito, uma apresentação, e uma convicção real de que ela deixa os times mais rápidos. Tenho tentado empurrar uma organização de engenharia numa direção. Este post é o que o empurrão me ensinou.

A metodologia é o AWS **[AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)**, o AI-Driven Development Lifecycle, apresentado no re:Invent 2025. A versão curta: a IA é uma colaboradora central sob supervisão humana. Ela planeja e executa, você segura as decisões. Sprints viram **bolts**, ciclos medidos em horas ou dias. O trabalho passa por três fases, inception, construção e operações. Um conjunto de **steering files** restringe como o agente trabalha, e eles viajam por qualquer IDE ou modelo que o desenvolvedor já use.

Eu não precisava ser convencido. Se você leu [o post sobre o loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/), o AI-DLC é quase a versão institucional do que eu já faço sozinho. Inception é brainstorm mais spec. Steering files são regras e não-objetivos. A AWS colocou um nome e um [repositório open source](https://github.com/awslabs/aidlc-workflows) numa coisa em que eu já acreditava. Então virei um defensor. Defender, acontece, é a parte fácil.

O discurso convence numa reunião. Cabeças acenam. Aí todo mundo volta para a sua mesa e trabalha do jeito que trabalhou na semana passada.

O abismo é a história de verdade. Então parei de discursar e comecei a ouvir os desenvolvedores que não tinham mudado. Aqui está o que ouvi, e nada disso é preguiça.

**Eles já se queimaram com processo imposto antes.** Todo engenheiro sênior já viveu um framework que prometeu velocidade e entregou cerimônia. Uma nova metodologia imposta casa com essa memória. O ceticismo é merecido.

**Os números de produtividade soam como marketing.** A AWS cita ganhos de 10 a 15 vezes. Para um cético profissional, um multiplicador que não dá para falsificar é uma razão para descartar, não para acreditar. Eles vão confiar num número quando o virem na própria base de código, e nem um segundo antes.

**O fluxo atual deles já funciona.** Um desenvolvedor rápido e eficaz tem um loop real rodando na cabeça. Pedir que ele troque por bolts e steering files é um custo concreto contra um retorno incerto. Manter o status quo é uma decisão racional.

**A saída da IA ainda precisa ser revisada.** Se você ainda não confia no agente, o AI-DLC move o seu trabalho de escrever código para revisar código. Eu trabalho num domínio regulado onde código errado tem consequências. A cautela por trás dessa hesitação está correta, não é medo.

**Veio de cima.** Uma metodologia empurrada por um arquiteto ou pela liderança dispara uma resposta humana simples. As pessoas adotam o que escolhem e resistem ao que lhes é atribuído. Eu era o de cima. Eu era o problema na minha própria adoção.

Olhe essas cinco de novo. Nenhuma é sobre preguiça ou medo de IA. Cada uma é sobre confiança ou atrito. Isso me parou, porque [o post anterior neste blog](/pt-br/posts/2026-05-20-frictionless-the-book-behind-the-loop/) era sobre um livro que diz exatamente isso. A confiança precisa ser construída, escrita e mantida. O atrito precisa ser encontrado e removido. Uma imposição não constrói confiança nenhuma e não remove atrito nenhum. Uma imposição só adiciona peso.

Então mudei o que eu estava fazendo. Algumas coisas de fato moveram as pessoas.

**Mostre, não conte.** Uma vitória real numa base de código real, a base de código do próprio time, supera toda apresentação que já fiz. Um cético não quer o meu número. Quer o dele.

**Mate a primeira semana.** A maioria das pessoas que abandona uma ferramenta a abandona nos primeiros dias, quando nada está configurado e tudo é atrito. Entregue os steering files já configurados. Faça a entrada levar minutos, não uma tarde.

**Faça do caminho padrão o bom caminho.** A adoção deve ser a escolha fácil, não a disciplinada. Se fazer certo exige força de vontade, não vai durar.

**Deixe os pares converterem os pares.** A adoção viaja de lado. Um engenheiro dizendo a outro "isso me poupou um dia" move mais do que qualquer arquiteto com um slide. Meu trabalho é criar esses momentos, não ser o mensageiro.

**Aceite um ritmo desigual.** Nem todo mundo muda de uma vez. Lutar contra isso reconstrói a imposição. Os primeiros a adotar puxam o próximo grupo, e o próximo grupo puxa o seguinte.

Aqui está o que eu errei desde o começo. O verbo era empurrar. Você não empurra um desenvolvedor para uma metodologia. Empurre com mais força e você obtém conformidade, do tipo raso, que some no momento em que você desvia o olhar. Os engenheiros que eu mais respeito não respondem a empurrão, e isso é uma qualidade de bons engenheiros, não um defeito.

Você não empurra. Você remove os motivos para dizer não, responde às objeções reais, torna o caminho melhor o mais fácil, e deixa o trabalho falar. Aí as pessoas caminham até lá por conta própria.

Empurrar é difícil porque empurrar é a física errada. Passei alguns meses aprendendo isso. A metodologia nunca foi a parte difícil. Eu fui.
