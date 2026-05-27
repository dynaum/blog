---
title: "Muitos Agentes, Um Chat"
subtitle: "Quando você roda mais de um agente localmente, você vira o gargalo. Uma interface de chat com um cofre é o upgrade. Por que agentchattr e Obsidian se combinam tão bem para o problema de escala pessoal."
date: 2026-05-27
description: "Escalando o setup local de desenvolvedor com agentchattr (uma interface de chat para trabalho multi-agente, cada agente na sua própria sessão tmux e worktree) e Obsidian como o plano e log de decisões do dia. O loop diário de duas superfícies, por que a metáfora do chat funciona, e o que o chat não resolve."
cover: /assets/img/2026-05-27-many-agents-one-chat.png
coverAlt: "Uma mesa escura e aconchegante à noite, um caderno aberto no centro ao lado de uma lanterna âmbar quente, com vários pequenos painéis de terminal brilhando flutuando no escuro ao redor. Um observador, um caderno, muitos agentes."
---

Quando você está rodando mais de um agente ao mesmo tempo, o gargalo deixa de ser o agente e passa a ser você, o orquestrador. Trocar entre quatro painéis de terminal, quatro worktrees e quatro contextos mentais é o novo imposto. Este post é sobre a ferramenta que paga esse imposto, e o loop diário que essa ferramenta torna possível.

Comecei esta série escrevendo numa única janela do Claude Code por vez. Oito posts depois eu estava rodando três ou quatro em paralelo via [git worktrees](/pt-br/posts/2026-05-25-pick-a-framework-any-framework/), e o ganho era real. O overhead de orquestração também. O próximo movimento foi uma interface de chat.

## A metáfora do chat

A metáfora do chat é a UI certa para gerenciar vários agentes localmente, porque desenvolvedores já sabem usar chat com humanos. Faça `@mention` neles, leia as mensagens deles, ignore quando você está fundo em outra coisa, deixe eles te chamarem quando travarem ou terminarem. A interface cognitiva já está montada.

O [agentchattr](https://github.com/bcurts/agentchattr) entrega essa metáfora de forma limpa. Grátis, local, um chat server mais uma UI web. Cada agente se auto-registra com sua própria identidade, cor, status pill, e roteamento de `@mention`. Cada agente roda dentro da sua própria sessão tmux, então sobrevive a um notebook fechado. Você reanexa com `tmux attach -t agentchattr-claude` quando quer a visão completa do terminal. Múltiplos provedores rodam em paralelo, então a ferramenta certa cabe na tarefa certa.

Menção honesta aos vizinhos. [multiagent-chat](https://github.com/estrada0521/multiagent-chat), [tmux-agents](https://github.com/super-agent-ai/tmux-agents), [agentic-tmux](https://github.com/negaga53/agentic-tmux), e [TMAI](https://github.com/trust-delta/tmai) vivem todos neste espaço. O agentchattr é o escolhido deste post porque a combinação chat mais tmux mais UI web é o encaixe local mais limpo hoje.

## O dia de duas superfícies

O chat é uma superfície. O cofre é a outra. Juntos formam a sala do time pessoal.

O blog já defendeu o [Obsidian como contexto compartilhado](/pt-br/posts/2026-05-22-your-ai-context-belongs-to-the-team/). Para o fluxo pessoal, o cofre carrega um segundo papel: o plano e o log de decisões do dia. Uma pasta `daily/`, uma nota por dia, com nome de data. A nota da manhã segura o plano: as intenções de hoje, em que cada agente vai trabalhar, como o sucesso se parece. Decisões tomadas no chat voltam para a nota do dia como linhas curtas. A pasta de princípios absorve o que for duradouro. A nota da manhã seguinte começa lendo a de ontem.

O chat é volátil. O cofre é durável. Sem o cofre, os agentes fazem o trabalho de hoje e nada disso sobrevive até amanhã.

## O loop diário

Concretamente, como um dia se parece com este setup.

1. **De manhã, no cofre.** Abra a nota do dia. Escreva as intenções do dia em um parágrafo. Decomponha cada uma numa spec ou num pedido claro. Decida qual agente fica com cada.
2. **Abra o chat.** Crie um agente por pedido. Cada um cai na sua própria sessão tmux e seu próprio worktree. Faça o briefing deles com o texto da spec do cofre.
3. **Durante o dia.** Alterne entre trabalho profundo e orquestração. O chat é onde os agentes falam com você e entre si. `@mention` para redirecionar. Deixe os outros rodando.
4. **Quando um agente trava.** Puxe a sessão tmux dele para o contexto completo do terminal. Decida, digite um redirecionamento de uma linha, desanexe, siga em frente.
5. **Fim de dia, de volta ao cofre.** Atualize a nota do dia com o que subiu, o que não subiu, as decisões que importam, as pegadinhas que valem a pena guardar.
6. **Amanhã.** A próxima nota do dia lê a de hoje, o cofre carrega os princípios atualizados no meio do caminho, e os agentes acordam para uma base de contexto que cresceu durante a noite.

Esse é o [loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) rodando em paralelo, com o chat como a camada de orquestração e o cofre como a memória.

Uma decisão escrita de volta para a nota do dia parece uma linha só: *"agente investigou o problema de rate-limit, causa raiz foi a falta de TTL na chave redis, fix no PR #234, subir depois da migração. Ver `principles/rate-limits.md` para a regra que saiu disso."* Essa frase é a memória do dia. É curta, é durável, a nota da próxima manhã a lê, e a pasta de princípios cresceu por uma.

Existe um custo de atrito neste setup. Disparar quatro agentes em vez de um significa quatro chances de um deles se perder. O cofre é o que pega quando se perdem, porque a spec está escrita, mas o custo é real. Dois ou três agentes é o ponto doce até você confiar no loop. Quatro é o limite antes do overhead de orquestração começar a morder de novo.

## Por que a metáfora do chat importa

Três razões.

**Familiaridade cognitiva.** Um desenvolvedor com quatro agentes em quatro abas de terminal está mentalmente rastreando quatro linhas. Um desenvolvedor com quatro agentes num chat está lendo um único fluxo. O chat colapsa N contextos numa única caixa de entrada. Mesma carga, menos imposto de troca de contexto.

**Roteamento por mention.** `@claude faz X` é um verbo que desenvolvedores já usam. A ferramenta que faz isso funcionar é uma daquelas pequenas escolhas de UI que somem assim que você as tem. O agente responde na própria thread. A thread é o registro.

**Visibilidade de status.** Cor, status pill, timestamp da última mensagem te dizem num piscar qual agente está rodando, qual está travado, qual está esperando por você. Esse é o dashboard que você queria, em vez de "dez janelas tmux, qual era a que tinha o teste quebrando."

## O que o chat não faz

Seção honesta. O chat não substitui nada do que este blog vem defendendo.

- O chat não é uma spec. Você ainda escreve o brief no cofre primeiro. O chat é onde você entrega.
- O chat não é memória. Conversas envelhecem, agentes resetam. O cofre é onde as coisas sobrevivem.
- O chat não é validação. Os agentes ainda produzem rascunhos. Você ainda revisa e decide. Mesma regra de todo outro post.
- O chat não é autonomia. Mesmo princípio de operador-no-loop do [post de operação](/pt-br/posts/2026-05-26-save-the-boring-time/). Agentes propõem, você decide.
- O chat não é um time mágico. Quatro agentes são quatro reports, não quatro colegas. Reports não têm o entendimento compartilhado que colegas constroem ao longo de anos. O cofre fecha parte dessa lacuna; nada fecha tudo.

O chat resolve o problema de orquestração. Ele não resolve o problema de disciplina.

## A mudança de papel

Um desenvolvedor com um editor e uma IDE é um codificador solo. Um desenvolvedor com quatro agentes num chat está mais perto de um líder de time com quatro reports. As ferramentas devem combinar com o papel. Uma inbox em estilo chat combina. Uma nota diária no cofre combina. O terminal ainda existe para o trabalho profundo, mas o centro de gravidade do dia se move para "orquestrar e validar" em vez de "digitar o próximo caractere."

Esse é o upgrade. A série vem construindo na direção do desenvolvedor pensando mais e digitando menos. agentchattr mais Obsidian é como esse dia se parece na escala local.

## Fechando

O framework escolhe o caminho. A fundação torna o caminho andável. Worktrees deixam você andar em muitos ao mesmo tempo. O chat coordena os caminhantes. O cofre impede que cada caminhada comece do zero.

O custo deste setup é uma tarde. O custo de não tê-lo aparece na terceira vez que você esquece qual janela tmux tinha o teste falhando.
