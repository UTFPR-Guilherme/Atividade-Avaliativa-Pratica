import unittest

from repositories.transaction_repository import TransactionRepository
from services.finance_service import FinanceService


class TestFinanceService(unittest.TestCase):

    def setUp(self):

        self.repository = TransactionRepository()

        self.service = FinanceService(self.repository)

    def test_register_transaction_success(self):

        self.service.register_transaction(
            "receita",
            1000,
            "Salário",
            "Pagamento"
        )

        transactions = self.repository.get_all_transactions()

        self.assertEqual(len(transactions), 1)

    def test_register_transaction_invalid_value(self):

        with self.assertRaises(ValueError):

            self.service.register_transaction(
                "despesa",
                -100,
                "Lazer",
                "Cinema"
            )

    def test_register_transaction_edge_case(self):

        self.service.register_transaction(
            "receita",
            0.01,
            "Extra",
            "Teste"
        )

        transactions = self.repository.get_all_transactions()

        self.assertEqual(transactions[0].value, 0.01)

    def test_calculate_balance_success(self):

        self.service.register_transaction(
            "receita",
            3000,
            "Salário",
            "Pagamento"
        )

        self.service.register_transaction(
            "despesa",
            1000,
            "Moradia",
            "Aluguel"
        )

        balance = self.service.calculate_balance()

        self.assertEqual(balance, 2000)

    def test_calculate_balance_empty_repository(self):

        balance = self.service.calculate_balance()

        self.assertEqual(balance, 0)

    def test_calculate_balance_edge_case(self):

        self.service.register_transaction(
            "receita",
            1000,
            "Salário",
            "Pagamento"
        )

        self.service.register_transaction(
            "despesa",
            1000,
            "Contas",
            "Pagamento"
        )

        balance = self.service.calculate_balance()

        self.assertEqual(balance, 0)


if __name__ == "__main__":
    unittest.main()