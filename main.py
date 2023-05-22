from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, w_type: str = 'General'):
        self.name = name
        self.w_type = w_type
        self.balance: int = 0

    def get_balance(self) -> int:
        return self.balance

    def change_balance(self, value: int):
        if self.balance + value < 0:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance += value


class CreditBalance:
    def change_balance(self, value: int):
        if self.balance + value < self.limit:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance += value


class ProBalance:
    def change_balance(self, value: int):
        if self.balance + value * 0.95 < 0:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance += value * 0.95 if self.balance + value * 0.95 < self.balance else value


class CreditCard(CreditBalance, Wallet):
    def __init__(self, name, limit=-1000):
        self.limit = limit
        super().__init__(name)

    # def change_balance(self, value: int):
    #     if self.balance + value < self.limit:
    #         print(f'Not enough balance {self.balance}')
    #     else:
    #         self.balance += value


class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)

    def change_type(self):
        if self.balance < 100:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance -= 100
            newcard = ProCard(name=self.name)
            newcard.balance = self.balance
            return newcard


class ProCard(ProBalance, Wallet):
    def __init__(self, name, w_type='PRO'):
        super().__init__(name, w_type)

    # def change_balance(self, value: int):
    #     if self.balance + value * 0.95 < 0:
    #         print(f'Not enough balance {self.balance}')
    #     else:
    #         self.balance += value * 0.95 if self.balance + value * 0.95 < self.balance else value


card = CreditCard(name='My_card')
print(card.get_balance())
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-900)
print(card.get_balance())
card.change_balance(100)
print(card.get_balance())
card.change_balance(-1000)
print(card.get_balance())

card.change_balance(1000)
print(card.get_balance())

# card = card.change_type()
# print(card.w_type)
