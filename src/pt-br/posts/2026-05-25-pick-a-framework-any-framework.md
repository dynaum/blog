---
title: "Escolha um Framework, Qualquer Framework"
subtitle: "AI-DLC é uma opção, não A opção. Quatro metodologias em 2026, a fundação que todas compartilham, e o upgrade de worktrees-e-orquestração que escala qualquer uma delas."
date: 2026-05-25
description: "Um panorama de quatro metodologias de desenvolvimento com IA em 2026 (AI-DLC, Superpowers, Spec-Kit, PRPs), as três fundações que todas compartilham, e a stack de git worktrees mais Claude Code Agent Teams mais Beads que as escala."
cover: /assets/img/2026-05-25-pick-a-framework-any-framework.png
coverAlt: "Uma parede de pedra escura à noite com quatro arcos e portas diferentes em fila, cada um com um formato diferente, todos abrindo para um espaço aquecido de luz âmbar lá dentro. Vários caminhos, mesmo destino."
---

Tenho sido o defensor barulhento de um framework há um tempo. Passar tempo de verdade com os outros me ensinou duas coisas. O framework importa menos do que eu pensava. E o upgrade que estava me faltando não estava no framework, estava em paralelizar o trabalho uma vez que a fundação estivesse no lugar.

Os quatro frameworks abaixo diferem em vocabulário, área de superfície, e profundidade de ferramentas. Eles convergem nos mesmos três movimentos:

1. **Descreva bem o problema.** Um usuário, uma dor, um porquê.
2. **Escreva uma spec.** Pitch, não-objetivos, critérios de sucesso, registro de decisões.
3. **Quebre o trabalho em passos.** Ordenados, testáveis, pequenos o suficiente para uma única execução do agente terminar um.

Times que fazem essas três coisas tiram valor de qualquer um dos frameworks. Times que pulam tiram uma bagunça mais rápida de todos eles.

O que importa de verdade é seguir o processo. Os frameworks ajudam porque **forçam** o processo. Assim como o [Docker](https://www.docker.com) força você a usar variáveis de ambiente em vez de configuração hardcoded, esses frameworks forçam você a escrever specs, nomear não-objetivos, e ordenar os passos antes do código. Sem um, a disciplina é opcional. Disciplina opcional apodrece. É por isso que pessoas que dizem "não preciso de framework" ainda se beneficiam de escolher um, mesmo de forma casual, porque o framework segura a linha nos dias em que você não seguraria.

## Os quatro

**[AWS AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/).** A versão institucional. Inception, depois Construction, depois Operations. Sprints viram **bolts**. **Steering files** restringem o agente. [Workflows open-source](https://github.com/awslabs/aidlc-workflows) no GitHub. Melhor encaixe quando a organização já vive na AWS, já roda Kubernetes, e está pronta para padronizar uma função inteira de engenharia numa única abordagem. O [post sobre adoção do AI-DLC](/pt-br/posts/2026-05-21-you-cannot-push-a-developer/) defendeu o uso dele. Este post o devolve ao contexto como uma opção, não a opção.

**[Anthropic Superpowers](https://github.com/obra/superpowers).** O framework aberto do [Jesse Vincent](https://github.com/obra), entregue como quatorze arquivos `SKILL.md` e um session hook. O workflow tem o mesmo formato sobre o qual este blog vem escrevendo: brainstorm, spec, plano, TDD, desenvolvimento por subagente, revisão, finalização. Funciona em [Claude Code](https://claude.com/claude-code), [Cursor](https://cursor.com), [OpenAI Codex](https://github.com/openai/codex), [Copilot CLI](https://github.com/github/gh-copilot), [Gemini CLI](https://github.com/google-gemini/gemini-cli), e [OpenCode](https://opencode.ai). [Plugin no marketplace da Anthropic](https://claude.com/plugins/superpowers). Cerca de 170 mil estrelas no GitHub até meados de 2026. Melhor encaixe quando você quer defaults opinativos fortes que dá para ler em Markdown puro e ajustar por projeto.

**[GitHub Spec-Kit](https://github.com/github/spec-kit).** Toolkit open-source agnóstico de agente. Um workflow limpo de quatro fases: spec, plan, tasks, code. Funciona em mais de 30 assistentes de IA para código. Melhor encaixe quando o time já está no ecossistema GitHub e quer infraestrutura mínima nova, uma CLI para colocar em qualquer repositório.

**[Product Requirements Prompts](https://github.com/coleam00/context-engineering-intro)** (PRPs, o padrão de context engineering). Não é um framework completo, é uma disciplina. Um PRP é um prompt engenheirado para consumo da IA, não um PRD escrito para humanos. Ele agrupa caminhos de arquivo, versões de biblioteca, exemplos de código, validation gates, e uma pontuação de confiança junto com a intenção. Melhor encaixe quando você não quer adotar uma nova metodologia, só uma forma mais afiada de escrever os prompts que você já escreve. Combina com qualquer um dos outros.

## Mesma física, vocabulário diferente

| | "descrever o problema" | "spec" | "passos" |
|---|---|---|---|
| **AI-DLC** | Inception | Inception artifacts + steering files | Bolts |
| **Superpowers** | Brainstorm | Spec | Plan + TDD + Subagent |
| **Spec-Kit** | Spec | Plan | Tasks |
| **PRPs** | Goal + justification | O PRP em si | Validation gates |

Os mesmos movimentos sustentando os quatro. Escolha o vocabulário que o seu time já fala.

## Por que agora

Não como pitch de venda, como observação.

Os quatro são open-source, mantidos, e têm comunidades barulhentas o suficiente para encontrar ajuda. O custo de um experimento é um branch e uma tarde. As ferramentas convergiram em specs em Markdown, interfaces agnósticas de agente, funcionando em vários IDEs. Um experimento que falha custa uma hora. Um que funciona muda como o time entrega.

Essa é a curva onde você para de assistir e começa a entregar.

## Escalando o trabalho

Um framework mostra o caminho. Andar nele uma vez é o ritmo de um desenvolvedor. Andar nele muitas vezes ao mesmo tempo é onde a mudança real aparece. Três camadas, de baixo para cima.

**Git worktrees, a primitiva.** Um [git worktree](https://code.claude.com/docs/en/worktrees) dá a cada agente seu próprio diretório de trabalho no mesmo repositório. Várias branches, um único histórico git, zero colisões de arquivo. O Claude Code tem suporte nativo via `--worktree` (`-w`) que cria o worktree, faz o branch, e inicia a sessão num passo só. O padrão é: especificar a feature, decompor em passos, criar um worktree por passo, revisar os diffs em ordem, dar merge.

A fundação é o que torna isso seguro. Spec ruim, agentes paralelos escrevendo interpretações conflitantes. Spec boa, agentes paralelos terminando numa tarde.

**Claude Code Agent Teams, a coordenação.** Worktrees dão isolamento. [Agent Teams](https://code.claude.com/docs/en/agent-teams) adiciona coordenação. Uma sessão do Claude Code age como team lead. Outras agem como colegas, cada uma na sua janela de contexto e no seu worktree, comunicando-se diretamente. Experimental, habilita-se setando `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` no `settings.json` ou no ambiente. A resposta de primeira mão da Anthropic para orquestração multi-agente, sentando naturalmente em cima dos worktrees.

UIs de orquestração de terceiros cobrem o mesmo terreno se você prefere um dashboard ou uma TUI. O [Conductor](https://conductor.build) da Melty Labs envolve o padrão worktree-por-agente num dashboard. O [Claude Squad](https://github.com/smtg-ai/claude-squad) envolve o mesmo padrão numa TUI tmux e suporta [Codex](https://github.com/openai/codex), [Aider](https://aider.chat), e [Gemini](https://github.com/google-gemini/gemini-cli) ao lado do Claude. Escolha a área de superfície que cabe no time.

**Beads, a memória.** Execuções paralelas longas batem em outro teto. Cada agente acorda sem memória do trabalho de ontem. [Beads](https://github.com/steveyegge/beads) do [Steve Yegge](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) é um issue tracker git-nativo, com SQLite, construído especificamente como memória para agentes de código. IDs por hash impedem colisões de merge entre branches. Decaimento semântico resume trabalho antigo para economizar contexto. Links de dependência entre tarefas sobrevivem entre sessões. Beads não é um framework, é o componente de memória que pareia com qualquer um deles.

A stack se lê de baixo para cima: fundação, framework, worktrees, coordenação, memória. Cada camada assume a de baixo.

## Fechando

Escolha o framework cujo vocabulário o seu time já fala. Faça as três fundações. Depois paralelize.

O framework mostra o caminho. A fundação é o que torna o caminho andável. Worktrees deixam você andar nele muitas vezes ao mesmo tempo. A coordenação impede que os caminhantes pisem uns nos outros. A memória impede que cada caminhada comece do zero.

Você não precisa de tudo isso no primeiro dia. Pegue um movimento de fundação que você pula hoje e adicione amanhã. Pegue um framework e tente numa funcionalidade real esta semana. O próximo movimento se abre sozinho.
