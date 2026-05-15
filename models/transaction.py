class Transaction:
    def __init__(self, transaction_type, value, category, description):
        self.transaction_type = transaction_type
        self.value = value
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.transaction_type} - R${self.value} - {self.category}"