from factories.transaction_factory import TransactionFactory

class FinanceService:

    def __init__(self, repository):
        self.repository = repository
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, total_expenses, limit):
        for observer in self.observers:
            observer.update(total_expenses, limit)

    def register_transaction(self, transaction_type, value, category, description):

        if value <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        transaction = TransactionFactory.create_transaction(
            transaction_type,
            value,
            category,
            description
        )

        self.repository.add_transaction(transaction)

    def calculate_balance(self):

        balance = 0

        for transaction in self.repository.get_all_transactions():

            if transaction.transaction_type == "receita":
                balance += transaction.value
            else:
                balance -= transaction.value

        return balance

    def calculate_total_expenses(self):

        total = 0

        for transaction in self.repository.get_all_transactions():

            if transaction.transaction_type == "despesa":
                total += transaction.value

        return total