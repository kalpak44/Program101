#CashDesk - problem
class CashDesk:

    def __init__(self):
        self.money = {100 :0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

    def take_money(self, money):        
        for coin in money:
            self.money[coin] += money[coin]

        

    def total(self):
        cash = 0
        for coin in self.money:
            cash += coin * self.money[coin]

        return(cash)




my_cash_desk = CashDesk()

my_cash_desk.take_money({100 :3, 50:1, 20:1})
my_cash_desk.total()
