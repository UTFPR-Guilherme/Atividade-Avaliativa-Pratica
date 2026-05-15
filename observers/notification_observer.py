class NotificationObserver:

    def update(self, total_expenses, limit):

        if total_expenses >= limit:
            print("ALERTA: Limite financeiro atingido.")