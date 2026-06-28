---
title: "Ela Me Deu um Formulário de Papel. Eu Criei um App."
subtitle: "Uma médica me pediu para anotar minha pressão arterial no papel por algumas semanas. Eu criei o app em vez disso. Levou uma tarde, e ele faz o único trabalho que o papel tinha, melhor."
date: 2026-06-28
description: "Numa consulta, a médica pegou um formulário de papel para eu acompanhar minha pressão arterial. Criei o bplog em vez disso: um PWA local-first com tendências e um relatório para o médico, código aberto, feito em uma tarde com IA. O custo de uma ferramenta pessoal ficou menor que o custo do atrito."
cover: /assets/img/2026-06-28-paper-form-built-an-app.png
coverAlt: "Um formulário de papel de pressão arterial sobre uma mesa escura sob luz âmbar quente cedendo lugar a uma tela de celular iluminada que mostra um gráfico de tendência limpo em ascensão, luz de contorno em teal, textura de pincelada e brilho suave."
---

Na minha última consulta, minha pressão arterial estava um pouco alta. Nada alarmante, mas o suficiente. A médica queria algumas semanas de dados antes de decidir qualquer coisa, então me pediu para medir duas vezes por dia e anotar. Aí ela pegou um bloco para me dar um formulário de papel.

Quase peguei. Aí parei. Por que papel?

## A conta virou

Pela maior parte da minha vida, papel era a resposta certa. Criar um app para acompanhar cinco números teria significado dias de configuração, um backend, uma tela de login, um banco de dados, um deploy. Tudo desproporcional à tarefa. O papel vencia porque a alternativa era absurda.

A conta é diferente agora. A configuração foi o que desmoronou, e com ela a razão inteira de pegar o bloco.

## O que eu criei

Eu criei o bplog. É um app de registro de pressão arterial para o seu celular. Duas medições por dia, manhã e noite, com um toque para marcar como você se sentiu. Roda no navegador, instala na sua tela inicial e funciona offline. Os números ficam no seu aparelho. Está no ar em [bplog.dynaum.com](https://bplog.dynaum.com) e é código aberto sob licença MIT.

## Uma tarde, não um projeto

Aqui está a parte que vale a pena destacar. Levou uma tarde.

Não porque seja um app trivial. Ele traça tendências de 7, 30 ou 90 dias. Classifica cada medição contra as faixas da American Heart Association. Gera um relatório para impressão para o médico. Exporta e restaura backups. Levou uma tarde porque eu não escrevi a maior parte à mão. Descrevi o que queria, e o modelo produziu a estrutura, os componentes, a ligação do gráfico, o service worker, os testes. React, Vite, TypeScript, Material 3. Sozinho, eu teria gasto o primeiro dia só reaprendendo a configurar um PWA. O modelo deixou tudo rodando antes do almoço.

É a ideia à qual eu sempre volto em [Construa Suas Próprias Ferramentas](/pt-br/posts/2026-05-28-build-your-own-tools/). O custo de uma ferramenta sob medida costumava ser a razão de você tolerar o atrito. Esse custo despencou. Quando construir a coisa certa é uma tarde, "conviva com o formulário de papel" deixa de ser a escolha racional.

## Rápido não significou desleixado

O medo com um app de uma tarde: ele é um brinquedo. Este não é.

O bplog é local-first por design. Suas medições vivem no armazenamento do navegador, no seu próprio aparelho. Sem conta, sem servidor, sem rastreamento, sem upload. O app não faz nenhuma chamada de backend com os seus dados. O formulário de papel tinha uma virtude silenciosa, ele era privado, e a maioria dos apps de saúde abre mão disso. Este mantém.

Ele também é acessível. Mira o WCAG 2.1 AA, traz uma verificação automática de acessibilidade na suíte de testes, evita que a cor seja o único sinal e dá ao gráfico um equivalente em tabela de texto para leitores de tela. A lógica de domínio, a classificação e a estatística, é testada de forma unitária, sem a interface no caminho.

Nada disso é exótico. É o que um app competente deveria fazer. O ponto é que uma construção de uma tarde passou nessa barra, porque o modelo carrega a amplitude que eu cortaria para economizar tempo.

## O relatório que vence o papel

O papel tinha um trabalho: entregar ao médico um registro na próxima consulta. Ele é ruim nisso. Um caderno é uma coluna de rabiscos. Uma foto do caderno é pior. O médico aperta os olhos, você lê números em voz alta, a tendência fica invisível.

O bplog tem um relatório para o médico. Uma página, imprime ou salva em PDF: o resumo, o gráfico, a divisão por categoria e uma tabela completa de cada medição. O médico lê em segundos e vê o formato do último mês, não uma pilha de dígitos. A ferramenta vence no exato trabalho para o qual o papel servia.

## O padrão deveria mudar

Ela pegou o papel porque papel é o padrão para "acompanhe isto você mesmo." Esse padrão é uma sobra de quando a alternativa era cara. Não é mais.

Não estou dizendo para criar um app para tudo. Muitas vezes papel ou um app que já existe é a escolha certa, e eu recorro aos dois. Estou dizendo que o limiar mudou, e a maioria das pessoas não atualizou onde acha que ele está. Quando o atrito é um formulário que você vai perder e uma foto que seu médico não consegue ler, e a solução é uma tarde, a resposta honesta é construir a solução.

## Use

O bplog é gratuito, código aberto e vive inteiramente no seu aparelho. Se uma médica ou médico um dia te entregar um formulário de papel para a sua pressão arterial, você tem outra opção.

Abra [bplog.dynaum.com](https://bplog.dynaum.com) no seu celular, adicione à tela inicial e registre uma medição. O código está no [GitHub](https://github.com/dynaum/bplog) se você quiser ler, fazer um fork ou torná-lo seu.
