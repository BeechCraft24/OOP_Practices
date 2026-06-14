class AccountException(Exception):
    pass

class BankAccount:
    AUDIT_LIMIT = 100_000

    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        raise AccountException("Account number cannot be changed.")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException("Balance cannot be negative.")
        self.__balance = value

    @balance.deleter
    def balance(self):
        if self.__balance != 0:
            raise AccountException("Cannot delete account with non-zero balance.")
        del self.__balance

    def deposit(self, amount):
        if amount > self.AUDIT_LIMIT:
            print("Audit message: large deposit operation detected.")

        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.AUDIT_LIMIT:
            print("Audit message: large withdrawal operation detected.")

        self.balance = self.balance - amount

account = BankAccount("ACC-001")

account.balance = 1000
print("Balance:", account.balance)

try:
    account.balance = -200
except AccountException as error:
    print("Error:", error)

try:
    account.account_number = "ACC-999"
except AccountException as error:
    print("Error:", error)

account.deposit(1_000_000)
print("Balance after deposit:", account.balance)

try:
    del account.balance
except AccountException as error:
    print("Error:", error)




class RouterConfig:
    def __init__(self):
        self.__ip_address = "192.168.1.1"

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value):

        if value.count(".") != 3:
            raise ValueError("Invalid IP address")

        self.__ip_address = value

router = RouterConfig()

router.ip_address = "101.0.0.1"
print(router.ip_address)