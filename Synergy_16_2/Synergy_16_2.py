class CashRegister:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount  
    
    def top_up(self, x):
        if x > 0:
            self.balance += x
        else:
            raise ValueError("Сумма пополнения должна быть положительной")
    
    def count_1000(self):
        return self.balance // 1000
    
    def take_away(self, x):
        if x <= 0:
            raise ValueError("Сумма изъятия должна быть положительной")
        if x > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= x
        return x
    
    def amount_print(self):
        return f"В кассе: {self.balance} руб."

kassa = CashRegister(5000)

print(kassa.count_1000())

print(kassa.take_away(1))

print(kassa.amount_print())