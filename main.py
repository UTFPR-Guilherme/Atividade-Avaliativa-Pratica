from repositories.transaction_repository import TransactionRepository
from services.finance_service import FinanceService
from observers.notification_observer import NotificationObserver

repository = TransactionRepository()

service = FinanceService(repository)

observer = NotificationObserver()

service.add_observer(observer)

service.register_transaction(
    "receita",
    3000,
    "Salário",
    "Pagamento mensal"
)

service.register_transaction(
    "despesa",
    1200,
    "Moradia",
    "Aluguel"
)

service.register_transaction(
    "despesa",
    500,
    "Alimentação",
    "Supermercado"
)

balance = service.calculate_balance()

print(f"Saldo atual: R${balance}")

expenses = service.calculate_total_expenses()

service.notify_observers(expenses, 1500)