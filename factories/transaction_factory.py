from models.transaction import Transaction

class TransactionFactory:

    @staticmethod
    def create_transaction(transaction_type, value, category, description):

        if transaction_type not in ["receita", "despesa"]:
            raise ValueError("Tipo de transação inválido.")

        return Transaction(
            transaction_type,
            value,
            category,
            description
        )