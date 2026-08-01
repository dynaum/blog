---
title: "kubeside: A Recusa É o Produto"
subtitle: "Um cliente Kubernetes feito para o desenvolvedor que entrega a aplicação, não para o operador que administra o cluster. Ele responde quatro perguntas e recusa todo o resto, e a recusa é a parte que vale discutir."
date: 2026-08-01
description: "Lançamento do kubeside, um cliente Kubernetes open source para desenvolvedores de aplicação. Quatro perguntas em qa, stg e prod, nada gravado em disco e uma longa lista de recursos recusados de propósito. Por que nomear a única pessoa que a ferramenta atende transforma a lista de recursos em um problema de subtração."
cover: /assets/img/2026-08-01-kubeside-launch.png
coverAlt: "Um campo denso de contêineres geométricos escuros sumindo na escuridão, com um corredor âmbar estreito cortando reto entre eles, iluminando apenas alguns contêineres ao longo do caminho enquanto o resto permanece apagado, luz de contorno azul-esverdeada nas bordas dos blocos, textura de pinceladas e brilho suave."
---

Três terminais abertos. Uma aba por réplica. E um palpite sobre qual versão a produção está rodando de verdade.

As perguntas nunca foram difíceis. Minha aplicação está no ar. O que mudou. O que os logs dizem. Qual configuração o contêiner recebeu. Ninguém construiu a tela para elas.

Hoje o kubeside é público.

## O formato errado

Toda interface de Kubernetes espelha a árvore da API. Escolha um tipo de recurso, navegue pelas instâncias, escolha um cluster num seletor. É o formato certo para quem administra o cluster. É o formato errado para quem entrega a aplicação.

Um desenvolvedor pensa em serviços, não em ReplicaSets. A unidade de trabalho dele é uma aplicação em qa, stg e prod. As perguntas dele são históricas com mais frequência do que ao vivo: o que mudou, quem mudou, o que o contêiner recebeu de fato. Então os dashboards viram atalhos para o `kubectl`, e quatro perguntas seguem sem resposta.

## Quatro perguntas

O kubeside responde exatamente essas quatro, lado a lado em todos os ambientes que o seu kubeconfig alcança.

```
$ kubeside --print
── kind-kubeside-demo  [live]  high risk
   NAMESPACE  APP             KIND        READY  GROUPED BY          WHY
■  team-b     search-indexer  Deployment  0/2    recommended-labels  pod search-indexer-75f4d is in ImagePullBackOff
●  team-a     checkout        Deployment  4/4    recommended-labels
●  team-b     billing         CronJob     —      workload-name
```

A saúde é derivada, e a linha diz o que a derivou. Um pod parado em `ImagePullBackOff` vale mais do que um ponto vermelho. A coluna `GROUPED BY` nomeia a regra por trás de cada linha, então uma lista com cara de errada mostra por que está com essa cara.

A tela que entrega o valor é a matriz de promoção. Uma linha por aplicação, uma coluna por ambiente. Uma versão que a produção tem e o staging não sobe para o topo, porque um hotfix que ninguém trouxe de volta é a pior coisa naquela tela. Mesma tag com digest diferente é sinalizada. Um ambiente que você não consegue ler diz `not readable`, o que não é a mesma coisa que `absent`.

## A recusa

Esta é a lista inteira do que o kubeside não faz. Sem visão de nós. Sem navegação de PersistentVolume. Sem editor de RBAC. Sem navegador de CRD. Sem gerenciamento de charts Helm. Sem relatório de custo. Sem grafo de topologia. Sem editor de YAML além de um visualizador somente leitura. Sem sistema de plugins.

Cada item é uma necessidade real que pertence à ferramenta de outra pessoa. Entregue qualquer um deles e isto vira um dashboard de propósito geral, que é justamente a coisa da qual já existe o bastante.

A lista é a decisão de produto. Escrevi as personas antes de existir qualquer código. Cinco pessoas que a ferramenta atende, e mais uma: a pessoa de plataforma, marcada no documento como parte interessada, não usuária. Todo item daquela lista é algo de que ela precisa, e nada disso foi entregue. As ferramentas dela são excelentes. Esta não é uma delas.

Nomeie a única pessoa que a ferramenta atende e a lista de recursos deixa de ser uma lista de desejos. Vira um problema de subtração. Cada não é uma tela que ninguém desenhou, um modelo de permissão sobre o qual ninguém raciocinou, uma suíte de testes que ninguém escreveu. Os nãos são a razão de dez dias terem bastado.

O mesmo movimento de [escrever a persona como uma regra](/pt-br/posts/2026-07-18-how-the-day-runs/) antes de entregar o trabalho a um agente, um nível acima. Lá ele mira uma sessão. Aqui ele desenha a fronteira de um produto.

## A aposta

O kubeside não grava nada em disco. Sem banco de dados, sem arquivo de cache, sem diretório de histórico. Pare o servidor e nada fica para trás.

Parece uma limitação até você ver o que isso obriga. A linha do tempo é reconstruída sob demanda a partir do histórico que o Kubernetes já guarda: ReplicaSets, ControllerRevisions, secrets de release do Helm, estados de término dos pods e eventos ainda dentro do TTL do apiserver. As mudanças carregam um autor lido do `managedFields`, então aquele `kubectl` que ninguém assume aparece do lado do rollout que ele causou.

Todo mundo assume que histórico precisa de armazenamento, então ninguém montou o histórico que o cluster já guarda. Estava ali o tempo todo.

A aposta rende duas vezes. Dois desenvolvedores abrem o kubeside durante o mesmo incidente e veem a mesma linha do tempo, porque ambos leem o mesmo cluster. Um banco local nunca poderia prometer isso.

## O que ele diz quando não sabe

A regra de que mais gosto: ausência de conhecimento não é ausência da coisa.

Onde a reconstrução acaba, o kubeside desenha um horizonte e o rotula.

```
replicaset · older rollouts pruned by revisionHistoryLimit; revision 11 is the oldest the cluster still holds
event      · older events have expired from the apiserver, which keeps roughly an hour by default
session    · kubeside started watching here; anything before this comes from the cluster's own history
```

Uma métrica que ele não conseguiu coletar é reportada como indisponível, nunca como zero. Um tipo que ele não conseguiu listar é nomeado. Um cluster que ele não alcança diz isso na própria linha, em vez de contribuir com silêncio para a lista de outra pessoa.

A mesma regra cobre permissões. Um controle que falta para você nunca é escondido. Ele fica visível, desabilitado, e nomeia o verbo que o cluster recusou. Um controle que some não ensina nada. Um que diz `needs create on pods/exec in team-a` mostra exatamente o que você precisa pedir.

Este é o [mesmo argumento sobre saber](/pt-br/posts/2026-06-09-it-never-knows-it-doesnt-know/) que o blog repete sobre modelos, aplicado a um dashboard. Uma ferramenta que desenha uma lacuna como um período tranquilo está mentindo para você na única hora em que você mais precisava dela honesta.

## Dez dias

Um binário Go com a interface embutida. Ele lê o kubeconfig que já está na sua máquina, carrega todos os contextos e roda plugins de credencial nativamente. Se o `kubectl` funciona, o kubeside funciona. Sem agente no seu cluster, sem instalador, sem passo de configuração. As credenciais ficam no processo, e o navegador só fala com `127.0.0.1`.

Oitenta commits, o primeiro dez dias antes deste post. Os testes vieram antes da implementação, e o repositório carrega hoje cerca de uma linha de teste por linha de código, em 518 funções de teste. A CI roda a suíte em Linux, macOS e Windows, porque compilar não é a mesma coisa que funcionar. Uma revisão de segurança passou pelos caminhos de escrita e pelo servidor local antes da v1.0.0, e tudo o que ela encontrou está corrigido.

A divisão de trabalho foi a de sempre. Eu fui dono do escopo, da lista de recusas e das regras sobre o que a ferramenta diz quando não sabe. O modelo foi dono da estrutura e da execução.

## Experimente

```
brew install dynaum/tap/kubeside
kubeside
```

Apache-2.0, no [GitHub](https://github.com/dynaum/kubeside), documentado em [kubeside.dynaum.com](https://kubeside.dynaum.com/).

Uma coisa ajudaria mais do que uma estrela. Rode `kubeside --print` contra um cluster cuja rotulagem ninguém controlou e me diga se a lista de aplicações bate com o que você chama de suas aplicações. Um cluster que agrupa quase tudo por `workload-name` é um cluster onde as convenções de rótulo não renderam nada, e isso é um achado sobre o cluster, não um defeito da ferramenta.

Esse agrupamento é a aposta inteira. Um cluster de demonstração limpo não prova nada, porque os rótulos dele são perfeitos por construção. Só o cluster bagunçado de outra pessoa resolve isso.
