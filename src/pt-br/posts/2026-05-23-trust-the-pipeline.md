---
title: "Confie no Pipeline"
subtitle: "Toda conversa de 'precisamos entregar mais rápido' é, na verdade, uma conversa de 'não confiamos no pipeline'. Cinco propriedades de um CI confiável, mais o setup de Playwright escrito por IA e Testkube que leva você até lá."
date: 2026-05-23
description: "QA é o gargalo que decide a vazão de entrega. As cinco propriedades de um pipeline confiável, o padrão grave-e-refine para testes Playwright escritos por IA, e onde o Testkube se encaixa acima do runner do CI."
cover: /assets/img/2026-05-23-trust-the-pipeline.png
coverAlt: "Um longo corredor de pedra escuro à noite com arcos recuando à distância, cada arco iluminado por uma pequena lanterna âmbar quente, o caminho rastreável por todos os portões."
---

Toda vez que alguém diz "precisamos entregar mais rápido", está dizendo outra coisa. Quer dizer: "não confio no pipeline."

Passei um ano empurrando por mais deploys por semana antes de entender a matemática. A vazão estava limitada por medo, não por mecânica. O deploy em si eram três comandos. O medo era o resto da conversa. Cada push para a fila era segurado por uma pergunta silenciosa, será que confiamos no pipeline para nos pegar se isto estiver errado.

A confiança no pipeline tem cinco propriedades, em ordem de importância.

**Determinístico.** Uma build vermelha significa uma falha real. Uma build verde significa seguro para subir. Flakiness é a primeira falha a corrigir, antes de qualquer outra, porque um único teste instável envenena toda build vermelha depois dele. As pessoas param de ler. As pessoas começam a re-rodar por palpite. Quando esse hábito se forma, você não tem mais sinal nenhum.

**Abrangente o suficiente.** O pipeline cobre os fluxos que importam, não todo método na base de código. Teatro de cobertura é pior do que nenhuma cobertura, porque entrega bug debaixo de um check verde. A pirâmide de testes é real, mas para vazão de entrega os testes que sustentam tudo são os fluxos ponta-a-ponta pelos quais o usuário caminha.

**Rápido o suficiente.** Feedback dentro da janela de fluxo de um desenvolvedor. Um pipeline de 45 minutos é um não-pipeline. Ele é agrupado, ignorado, contornado com checagens manuais. Abaixo de 10 minutos é o alvo. Abaixo de 5 é a vitória.

**Com dono.** Cada teste pertence a uma pessoa ou a um padrão claramente nomeado. Testes órfãos apodrecem, testes apodrecidos são pulados, e testes pulados são como regressões passam. O padrão importa mais do que o próprio teste.

**Honesto.** Nenhuma anotação `.skip` escondendo regressões. Nenhuma gaveta de quarentena de "a gente conserta depois". Nenhuma build verde cobrindo uma falha conhecida. Se um teste está quebrado, conserte ou apague. O meio-termo destrói a confiança.

Um pipeline com as cinco ganha confiança. Um pipeline faltando qualquer uma não ganha. Sem confiança, todo deploy vira uma reunião.

Eu trabalho num domínio regulado onde código errado tem consequências. O custo de um pipeline sem confiança ali não é só entrega mais lenta, é a reunião virando o mecanismo de segurança. Isso é insustentável, e transforma o argumento pela confiança num argumento sobre segurança, não sobre velocidade.

Então a pergunta vira: como você constrói essa confiança no ritmo em que as funcionalidades entregam? Escrever os testes é um gargalo. Rodá-los é o outro. A IA muda o primeiro, o Testkube muda o segundo.

**Grave, depois refine.**

A maneira errada de usar IA para testes é pedir que o modelo escreva um do zero. "Escreva um teste Playwright para o fluxo de checkout." O modelo alucina seletores, inventa asserções que passam por acidente, gera `await page.waitForTimeout(2000)` porque às vezes funciona. Você integra o teste. Ele passa. Depois ele falha de vez em quando. Você deixa de confiar nele. De volta à estaca zero.

A maneira certa é o loop guiado por spec aplicado a testes. Grave a interação real primeiro com `playwright codegen` ou uma sessão do [Playwright MCP](https://github.com/microsoft/playwright-mcp), depois peça ao modelo para refinar a gravação em Playwright idiomático. A gravação é a spec. O modelo reescreve para as regras:

- Seletores usam `getByRole`, `getByLabel`, `getByTestId`. Nunca `nth`, `first`, `last`, ou cadeias de classes CSS.
- Apenas asserções web-first. `await expect(locator).toBeVisible()`, não igualdade pura.
- Nada de `waitForTimeout`. O modelo adora. O modelo está errado.
- Passos repetidos extraem para helpers. Um teste, uma preocupação.

O arquiteto é dono da intenção e da revisão. O modelo é dono da reescrita. Um teste gerado é um rascunho, não um commit.

**Testkube acima do runner.**

Escrever testes é um gargalo. Rodá-los é o outro, e é mecânico. Uma suíte Playwright de 200 testes num único runner do GitHub Actions é uma execução serial de 25 minutos. A mesma suíte fatiada em 20 pods é 90 segundos. A propriedade três vive ou morre nessa lacuna.

O [Testkube](https://testkube.io/) é uma plataforma de orquestração de testes nativa do Kubernetes. Ele roda os mesmos testes Playwright, mas como cargas de trabalho no seu cluster, com sharding e paralelismo cuidados para você, e com traces, vídeos, logs e histórico de flakiness vivendo num lugar que não evapora quando o job de CI termina. O job de CI desaba para uma única linha: dispara o Testkube, espera, decide com base no resultado. A complexidade de teste sai do YAML e vai para um lugar feito para escalar.

Seja honesto quanto ao encaixe. O Testkube é a resposta certa quando você já vive no Kubernetes, quando um runner não dá o paralelismo que você precisa, ou quando os artefatos do teste precisam sobreviver ao run do CI. Se você está num projeto pequeno no Vercel sem cluster, o Testkube é mais plataforma do que o problema merece. A ferramenta honesta ali é uma matrix do GitHub Actions.

**O fio de volta para a série.**

[Frictionless](/pt-br/posts/2026-05-20-frictionless-the-book-behind-the-loop/) acrescenta Confiança como a nova métrica para a era da IA. As cinco propriedades acima são como Confiança fica dentro de um pipeline de CI.

As quatro regras do Playwright são exatamente os steering files dos quais [o post sobre AI-DLC](/pt-br/posts/2026-05-21-you-cannot-push-a-developer/) falou. Um conjunto de restrições que o agente tem de honrar quando gera testes, escrito uma vez, reutilizado para sempre.

O lugar onde essas regras moram, junto com as fixtures, os helpers, a convenção de testid, é a camada de contexto compartilhado do [post anterior](/pt-br/posts/2026-05-22-your-ai-context-belongs-to-the-team/). Um pipeline só permanece confiável porque as convenções que produzem testes confiáveis são escritas uma vez e lidas por toda sessão futura.

É o [loop guiado por spec](/pt-br/posts/2026-05-19-the-spec-driven-loop/) de novo, mais uma camada de runtime para escalar.

Você não desbloqueia entrega entregando mais. Você desbloqueia confiando no portão que decide se você pode. A confiança vem das cinco propriedades, não de um truque. A IA ajuda você a escrever mais dos testes que a ganham. O Testkube dá a esses testes um lugar para rodar que não trava o pipeline em que você está tentando confiar.

Toda outra melhoria de entrega é consequência disso.
