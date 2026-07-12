---
title: "O tmux Continua Funcionando. Eu Troquei Mesmo Assim."
subtitle: "Nada quebrou. O meu trabalho mudou de formato, a ferramenta não mudou, e depois de anos com o mesmo setup eu quis descobrir se ainda era capaz de me mexer."
date: 2026-07-11
description: "Usei tmux por anos e ele nunca me deixou na mão. Depois o meu terminal encheu de agentes de código que eu preciso supervisionar em vez de comandos que eu digito, e uma ferramenta construída para isso desde o primeiro dia ganhou de uma ferramenta se adaptando a isso. A troca foi pequena. O hábito por trás dela não é."
cover: /assets/img/2026-07-11-tmux-still-works.png
coverAlt: "Uma ferramenta manual gasta, de cabo de madeira, deitada sobre uma bancada escura, ainda limpa e utilizável, enquanto uma mão passa por ela para pegar um instrumento de precisão mais novo, com um brilho âmbar quente entre os dois e uma luz de contorno azul-esverdeada, textura de pincelada e leve bloom."
---

O tmux nunca me deixou na mão. Nenhuma vez, em anos. Sem crash, sem perda de dados, sem uma manhã em que as minhas sessões tivessem sumido. E foi exatamente isso que tornou a saída difícil.

Uma ferramenta quebrada pede para ser substituída. Uma ferramenta que funciona não pede nada. Você mantém a memória muscular, mantém a config que ajustou em 2019, e nunca descobre o que mais existe. Fiquei ali por muito tempo, confortável, e conforto é um péssimo motivo para parar de olhar em volta.

Semana passada eu instalei o [herdr](https://herdr.dev/) e movi o meu trabalho diário para ele.

## A ferramenta não mudou. O trabalho mudou.

O meu terminal costumava ser um lugar onde eu digitava. Comandos, testes, um servidor à esquerda, logs à direita. Os painéis eram recipientes para coisas que eu iniciava e acompanhava com os meus próprios olhos.

Não é mais isso que eu faço o dia inteiro. Agora eu rodo agentes de código. Vários ao mesmo tempo, em repositórios diferentes, em branches diferentes. Um está rodando uma suíte de testes. Outro está no meio de um refactor. Outro parou quatro minutos atrás e está esperando eu responder uma pergunta, e eu não faço ideia, porque um painel tem a mesma cara com um agente trabalhando duro ou parado pedindo permissão.

O gargalo mudou de lugar. Eu não sou lento para digitar. Eu sou lento para saber qual dos meus agentes precisa de mim agora.

O tmux não tem opinião nenhuma sobre isso, e nem deveria ter. Ele é um multiplexador de terminal, e dos bons. Ele me dá painéis e sessões e sai do caminho. O estado dentro desses painéis não é da conta dele, por projeto.

## Construído para isso ganha de adaptado para isso

O herdr parte de outra premissa. É um multiplexador em que o workspace sabe que existem agentes rodando dentro dele.

Cada painel carrega um estado: parado, trabalhando, bloqueado, concluído. Uma barra lateral mostra todos de uma vez. Eu olho para uma coluna e vejo o formato do rebanho inteiro. O agente esperando por uma decisão aparece marcado como esperando por uma decisão. Parei de descobrir sessões bloqueadas três minutos atrasado, girando entre painéis.

Esse é o benefício inteiro, e no papel ele soa pequeno. Na prática, muda como o dia funciona. A minha atenção vai para o agente que está pedindo por ela, em vez de ir para uma varredura em círculo de seis painéis torcendo para achar alguém travado.

O ecossistema em volta do tmux está se adaptando. Gambiarras na status line, scripts wrapper, plugins para expor o estado do agente. Tem gente construindo a mesma ideia em cima de uma ferramenta que nunca foi desenhada para isso, e alguns desses setups são espertos. Mas existe diferença entre uma ferramenta se curvando na direção do seu trabalho e uma ferramenta que já começa onde o seu trabalho está. A primeira pede que você monte a resposta. A segunda já vem com ela.

## A parte de que ninguém gosta

Os dois primeiros dias foram piores. Óbvio que foram piores.

As minhas mãos conhecem o tmux. A tecla de prefixo dispara antes do pensamento. Eu batia nela o tempo todo no herdr e nada acontecia, do mesmo jeito que você procura o interruptor de luz numa casa da qual já se mudou. Algum canto da minha config antiga, ajustada ao longo de anos, ainda não foi reproduzido em lugar nenhum. Me senti lento, e ser lento em algo em que você era rápido é uma humilhação pequena e bem específica.

Depois passou. Dois dias. Esse foi o preço inteiro.

Compare com o que os anos sem olhar em volta me custaram. Eu rodava um fluxo cheio de agentes dentro de uma ferramenta que não tinha ideia de que agentes existiam, e chamava aquele atrito de normal, porque não tinha nada com que comparar. O custo de trocar é barulhento, visível e acaba em uma semana. O custo de nunca trocar é silencioso e vai se acumulando. Você não sente. Você simplesmente vira, aos poucos, alguém cujo setup foi desenhado para o trabalho que fazia em 2019.

## O hábito não é sobre o multiplexador

Eu não estou dizendo para você instalar o herdr. Talvez tmux com um bom plugin seja a resposta certa para você. Talvez você tenha testado o herdr e odiado.

Estou dizendo que a troca nunca foi sobre um multiplexador. Foi um teste para saber se eu ainda sou alguém que se move. Fazer a mesma coisa por anos não significa necessariamente que você parou de aprender, mas escorrega para lá em silêncio, e ninguém te manda uma notificação quando acontece. Você descobre depois, quando uma categoria inteira de ferramenta passou por você e você não levantou a cabeça.

Então levante a cabeça de propósito. De vez em quando, pegue a coisa construída para o trabalho que você faz hoje, e veja se o chão se moveu.

Depois olhe para a sala onde você está sentado. Se o seu time faz o mesmo trabalho do mesmo jeito de três anos atrás, e tudo que é novo é recebido com "o que a gente tem já funciona", pergunte a si mesmo honestamente o que você está aprendendo ali. Uma ferramenta que funciona não pede nada de você. Uma empresa confortável também não. As duas te deixam parado enquanto a área se move, e uma delas está custando uma carreira, não um arquivo de config.

Eu sei qual das duas eu deixaria para trás.

Posso voltar para o tmux mês que vem. Se voltar, vai ser porque eu sei, não porque nunca fui verificar.
