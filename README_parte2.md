# Atividade-Avaliativa-Pratica-Parte-2

## Tarefa 2.1 — Definição da Arquitetura
Defini para o desenvolvimento do projeto o padrão de Arquitetura em Camadas. Esse padrão foi escolhido por permitir uma separação clara das responsabilidades do sistema, facilitando a organização do código, manutenção e evolução futura da aplicação.

A arquitetura em camadas se adequa bem ao domínio do projeto, pois o sistema possui funcionalidades relacionadas ao cadastro, organização e processamento de informações financeiras. Além disso, as histórias de usuário definidas na Parte 1 exigem separação entre interface, regras de negócio e gerenciamento de dados, principalmente nas funcionalidades de registro de transações financeiras e categorização de despesas.

## Representação dos componentes:
Usuário
   ↓
Interface (main.py)
   ↓
FinanceService
   ↓
TransactionRepository
   ↓
Lista de Transações

## Models:
- Transaction
- Category

## Padrões utilizados:
- Factory Method
- Observer

## Componentes principais e responsabilidades:
main.py: Responsável pela interação com o usuário, entrada de dados e execução do fluxo principal do sistema.

FinanceService: Responsável pelas regras de negócio do sistema, como cadastro de transações, cálculo de saldo, categorização de despesas e verificação de limites financeiros.

TransactionRepository: Responsável pelo armazenamento e gerenciamento das transações cadastradas no sistema.

Transaction: Representa uma movimentação financeira do sistema, contendo informações como valor, categoria, descrição e tipo da transação.

Category: Representa as categorias financeiras utilizadas para organizar as despesas.

TransactionFactory: Responsável pela criação de objetos de transação utilizando o padrão Factory Method.

NotificationObserver: Responsável por monitorar alterações financeiras e emitir alertas quando limites de gastos forem atingidos.

## Limitações e trade-offs da arquitetura:
Apesar da Arquitetura em Camadas facilitar a organização do sistema, ela pode aumentar a quantidade de arquivos e classes mesmo em aplicações pequenas, tornando o desenvolvimento inicial mais demorado.

## Minha Reflexão: [A Arquitetura em Camadas foi escolhida principalmente pela simplicidade de implementação e pela boa separação de responsabilidades entre os componentes do sistema. Apesar da arquitetura em camadas talvez não ser a mais "otimizada", para o nosso objetivo da atividade, ela se encaixa perfeitamente, um sistema pequeno, de implementação rápida e que cumpra todos os requisitos de organização, padrões de projeto e testes.]

## Tarefa 2.2 - Implementação com Padrões de Projeto

## Padrão 1 — Factory Method

## Categoria: 
Criacional.

## Objetivo do padrão:
O padrão Factory Method foi utilizado para centralizar a criação das transações financeiras do sistema. Sua utilização permite desacoplar a lógica de criação dos objetos da camada principal de regras de negócio, facilitando manutenção e futuras expansões do sistema.

No contexto do projeto, o padrão foi aplicado para criar objetos de receita e despesa de forma padronizada e validada antes do armazenamento no sistema.

## Diagrama do padrão aplicado ao projeto:
FinanceService
      ↓
TransactionFactory
      ↓
Transaction

## Onde foi aplicado no código:
factories/transaction_factory.py

## Trecho relevante:
transaction = TransactionFactory.create_transaction(
    transaction_type,
    value,
    category,
    description
)

## Padrão 2 — Observer

## Categoria: 
Comportamental.

## Objetivo do padrão:
O padrão Observer foi utilizado para monitorar alterações relacionadas aos gastos financeiros do usuário e emitir alertas quando determinados limites forem atingidos. Esse padrão permite desacoplar o sistema de notificações da lógica principal da aplicação, facilitando futuras expansões no mecanismo de alertas.

No projeto, observadores são registrados no serviço financeiro e notificados sempre que o sistema verifica os gastos totais do usuário.

## Diagrama do padrão aplicado ao projeto:
FinanceService
      ↓ notifica
NotificationObserver

## Onde foi aplicado no código:
observers/notification_observer.py

## Trecho relevante:
def notify_observers(self, total_expenses, limit):
    for observer in self.observers:
        observer.update(total_expenses, limit)

## Revisão crítica:
Apesar do Observer facilitar a separação entre a lógica financeira e o sistema de notificações, ele pode se tornar difícil de manter conforme o sistema cresce e novos tipos de alertas são adicionados. Em um projeto maior, muitos observadores diferentes poderiam aumentar a complexidade da comunicação interna e dificultar a identificação de erros relacionados às notificações. Além disso, novos membros da equipe poderiam ter dificuldade para rastrear quais componentes estão sendo notificados em determinados eventos do sistema.

## Histórias de usuário implementadas
- História 1: Registro de receitas e despesas.
- História 2: Categorização de despesas.

## Tarefa 2.3 - Testes

## Estratégia de testes:
Os testes automatizados foram desenvolvidos utilizando a biblioteca unittest do Python, com foco principal na validação das regras de negócio mais importantes do sistema financeiro. Foram testados os métodos de registro de transações e cálculo de saldo, pois ambos estão diretamente relacionados às histórias de usuário de maior prioridade definidas na Parte 1.

A estratégia adotada buscou cobrir cenários de sucesso, falha e casos de borda, garantindo que o sistema se comporte corretamente em diferentes situações de uso. Os testes verificam tanto o funcionamento esperado quanto o tratamento de entradas inválidas e situações limite.

Alguns aspectos do sistema não foram cobertos pelos testes, como notificações do padrão Observer e interação com interface de usuário. Isso ocorre porque o protótipo possui foco principal nas regras centrais de negócio e não em integração completa entre componentes externos.

## Revisão crítica:
Uma das partes mais difíceis de testar no sistema seria o mecanismo de notificações implementado com o padrão Observer. Em um projeto maior, diferentes observadores poderiam reagir de formas distintas aos eventos financeiros, aumentando a complexidade para validar comportamentos assíncronos e dependências entre componentes. Além disso, testes envolvendo notificações externas, como e-mails ou mensagens em tempo real, exigiriam ambientes de simulação e isolamento mais sofisticados.

## Críticas finais do projeto/atividade:
Achei o projeto muito interessante, pois permitiu compreender de maneira prática todo o processo de desenvolvimento de uma aplicação, desde o levantamento de requisitos até a implementação e testes. A atividade ajudou a demonstrar a importância de analisar, pesquisar, documentar, validar requisitos e estruturar corretamente um sistema antes de iniciar a codificação.

Além disso, foi possível entender melhor como boas práticas de engenharia de software, padrões de projeto, organização de código, testes automatizados e versionamento contribuem para a construção de aplicações mais organizadas, escaláveis e fáceis de manter.

Outro ponto que considerei muito positivo foi a utilização de ferramentas modernas, como IA e GitHub, aproximando a atividade de um cenário mais próximo da realidade do mercado de desenvolvimento atual. Isso tornou a experiência mais dinâmica, prática e útil tanto para avaliação do professor quanto para o aprendizado dos alunos.

## *Em alguns momentos na conversa com a IA, eu colo o texto que eu mesmo escrevi, como por exemplo a revisão crítica e peço apenas para ele melhorar, revisar e aprovo, mas é minha ideia;

## Como executar o projeto:
Dentro da pasta execute - python main.py

## Executando os testes:
python -m unittest

Conversa com IA: [https://chatgpt.com/share/6a03757d-56e8-83e9-927c-b1c5d49f7dc1]