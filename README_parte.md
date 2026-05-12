# Atividade-Avaliativa-Pratica

Tarefa 1.1, Proposta de Tema

Sistema de Controle Financeiro

Problema que o sistema resolve: Meu sistema busca ajudar pessoas que possuem dificuldade em organizar e acompanhar suas finanças pessoais, oferecendo uma forma simples de controlar gastos, visualizar despesas e manter maior consciência sobre a própria situação financeira.

Quem são os usuários principais: Quem são os usuários principais: Adultos economicamente ativos, acima dos 18 anos, que desejam melhorar o controle das próprias finanças e organizar melhor seus gastos do dia a dia.

Por que esse problema é relevante: A organização financeira ainda recebe pouca atenção de muitas pessoas, mesmo tendo impacto direto na estabilidade e qualidade de vida. Atualmente, grande parte dos brasileiros enfrenta dificuldades para controlar gastos, economizar e manter um planejamento financeiro consistente, muitas vezes por falta de conhecimento financeiro ou de ferramentas simples que auxiliem nessa organização do dia a dia.

--------------------------------------------

Tarefa 1.2, Planejamento de Entrevista

Pergunta 1: Como você descreveria sua organização financeira atualmente? Quais são as principais dificuldades que você enfrenta no dia a dia?

Pergunta 2: Atualmente, você consegue ter controle de todas as suas receitas, despesas e transações mensais?

Pergunta 3: O que mais dificulta ou impede você de melhorar sua organização financeira hoje?

Pergunta 4: Quais tipos de gastos mais impactam seu orçamento mensal? Existem despesas que você considera desnecessárias ou difíceis de controlar?

Pergunta 5: Como funciona sua rotina em relação ao acompanhamento das suas finanças pessoais?

Pergunta 6: Você já utilizou algum aplicativo, planilha ou ferramenta de controle financeiro? Como foi sua experiência?

Pergunta 7: Você costuma acessar informações financeiras com mais frequência pelo celular ou computador? Por quê?

Pergunta 8: Quais funcionalidades ou características você considera essenciais em um aplicativo de controle financeiro?

Minha reflexão: [Aqui eu tentei explorar algumas perguntas sobre a vida "pessoal"/financeira da pessoa, sem invadir muito, para descobrir os principais problemas da minha persona, assim pensando em soluções no desenvolvimento do aplicativo. Com esses dados, posso atacar exatamente em pontos perfeitos que sei que vão resolver as dores dos meus clientes.]

--------------------------------------------

Historias de Usuario

História 1

Como usuário, quero registrar minhas receitas e despesas para acompanhar meu saldo financeiro mensal.

Critérios de aceitação
O sistema deve permitir cadastrar receitas e despesas manualmente.
Cada transação deve possuir valor, categoria, descrição e data.
O saldo mensal deve ser atualizado automaticamente após cada registro.
Prioridade: Alta

Essa funcionalidade é essencial para o funcionamento do sistema, pois o controle financeiro depende diretamente do registro das movimentações financeiras do usuário. Sem isso, as demais funcionalidades perdem sentido.

História 2

Como usuário, quero categorizar minhas despesas para identificar em quais áreas estou gastando mais dinheiro.

Critérios de aceitação
O sistema deve permitir selecionar categorias para cada despesa.
O usuário deve visualizar os gastos separados por categoria.
O sistema deve permitir criar novas categorias personalizadas.
Prioridade: Alta

A categorização ajuda o usuário a entender seus hábitos financeiros e identificar gastos excessivos. Essa funcionalidade complementa diretamente o controle das transações financeiras.

História 3

Como usuário, quero visualizar gráficos e relatórios financeiros para analisar meu comportamento de gastos ao longo do mês.

Critérios de aceitação
O sistema deve exibir gráficos de despesas e receitas.
Os relatórios devem apresentar informações mensais organizadas.
O usuário deve conseguir visualizar o total gasto em cada categoria.
Prioridade: Média

Os gráficos e relatórios auxiliam na análise financeira, mas o sistema ainda conseguiria cumprir sua função principal sem essa funcionalidade em uma primeira versão.

História 4

Como usuário, quero receber alertas de gastos excessivos para evitar ultrapassar meu orçamento mensal.

Critérios de aceitação
O sistema deve permitir definir um limite de gastos mensal.
O usuário deve ser notificado ao atingir determinado percentual do limite.
Os alertas devem informar o valor já gasto no período.
Prioridade: Média

Os alertas ajudam o usuário a tomar decisões financeiras mais conscientes, porém não são indispensáveis para o funcionamento básico do sistema.

História 5

Como usuário, quero acessar meu sistema financeiro pelo celular para acompanhar minhas finanças em qualquer lugar.

Critérios de aceitação
O sistema deve possuir interface adaptada para dispositivos móveis.
O usuário deve conseguir registrar movimentações pelo celular.
As informações devem ser sincronizadas automaticamente entre dispositivos.
Prioridade: Baixa

Embora a acessibilidade mobile melhore bastante a experiência do usuário, ela não é prioridade inicial quando comparada às funcionalidades principais de registro e organização financeira.

Minha reflexão: [Aqui usei a IA para me ajudar a gerar 5 histórias de usuário para meu sistema, mandando tudo que tinha feito até a tarefa 1.2, assim apenas conferi as histórias feitas por ele, adaptei pequenos detalhes e aprovei, achando coerente com o que estamos buscando.]

--------------------------------------------

Tarefa 1.4, Validação de Requisitos

Validação da História 1:
Como usuário, quero registrar minhas receitas e despesas para acompanhar meu saldo financeiro mensal.

Ambiguidades identificadas:
O critério “o saldo mensal deve ser atualizado automaticamente após cada registro” pode gerar interpretações diferentes, pois não especifica se a atualização acontece instantaneamente ou após algum processamento interno do sistema.

Além disso, o critério “cada transação deve possuir valor, categoria, descrição e data” não deixa claro quais campos serão obrigatórios e quais poderão ser opcionais no cadastro da movimentação financeira.

Possíveis conflitos com outras histórias:
Pode existir conflito com a História 2, relacionada à categorização de despesas, pois a História 1 não especifica se receitas também poderão possuir categorias ou apenas despesas.

Também pode existir conflito com a História 5 caso a sincronização entre dispositivos não aconteça corretamente, afetando a atualização do saldo em tempo real.

Informações que precisam ser esclarecidas junto ao usuário:
O usuário poderá editar ou excluir transações já cadastradas?
O sistema permitirá registrar despesas parceladas?
O saldo será atualizado em tempo real em todos os dispositivos?
Todas as movimentações precisarão obrigatoriamente de categoria?

---

Validação da História 4:
Como usuário, quero receber alertas de gastos excessivos para evitar ultrapassar meu orçamento mensal.

Ambiguidades identificadas:
O critério “o usuário deve ser notificado ao atingir determinado percentual do limite” é vago, pois não especifica qual percentual será utilizado nem se ele poderá ser personalizado pelo usuário.

O critério “os alertas devem informar o valor já gasto no período” também não define claramente qual período será considerado, como mensal, semanal ou diário.

Possíveis conflitos com outras histórias:
Pode existir conflito com a História 3, responsável pelos relatórios financeiros, caso os valores apresentados nos alertas sejam diferentes dos exibidos nos gráficos e relatórios.

Também pode haver conflito com a História 5, já que notificações podem funcionar de maneiras diferentes entre celular e computador.

Informações que precisam ser esclarecidas junto ao usuário:
O usuário poderá configurar diferentes limites de gastos?
Os alertas serão enviados por notificação, e-mail ou dentro do sistema?
O orçamento será único ou separado por categoria?
O usuário poderá desativar os alertas?

Revisão crítica

Se o escopo do projeto precisasse ser reduzido, eu removeria a História 3, relacionada aos gráficos e relatórios financeiros. Apesar de ser uma funcionalidade útil para análise visual e acompanhamento mais detalhado das finanças, ela não é essencial para o funcionamento principal do sistema, que é permitir o registro e organização das movimentações financeiras do usuário. Além disso, essa funcionalidade exigiria uma complexidade maior no desenvolvimento, envolvendo filtros, geração de dados estatísticos e visualizações gráficas. As demais histórias se encaixam melhor em um MVP viável, mantendo as funções mais importantes para resolver o problema principal do usuário.

Conversa com IA: [https://chatgpt.com/share/6a03757d-56e8-83e9-927c-b1c5d49f7dc1]
*Em alguns momentos na conversa com a IA, eu colo o texto que eu mesmo escrevi, como por exemplo a revisão crítica e peço apenas para ele melhorar, revisar e aprovo, mas é minha ideia;