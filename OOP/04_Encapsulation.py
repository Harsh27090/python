# hiding details from outside
class BankAccount:

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance # private variable - cannot be accessed from outside
        print(f'Bank account created with acc. no.:{acc_no}, name:{name}, balance:{balance}')

    def deposit(self,amount):
        self.__balance += amount
        print(f'Deposited {amount} to {self.acc_no}')

    def withdraw(self,amount):
        self.__balance -= amount
        print(f'Withdrawed {amount} from {self.acc_no}')

    def get_balance(self):
        return self.__balance

acc1 = BankAccount('12345', 'Harsh', 5000)
acc1.deposit(2000)
print(f'Current balance is: {acc1.get_balance()}')
acc1.withdraw(3000)
print(f'Current balance is: {acc1.get_balance()}')