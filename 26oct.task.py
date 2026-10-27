class Bank_Account:
    def __init__(self, name, bank_name, account_no, balance):
        self.__name = name
        self.__bank_name = bank_name
        self.__account_no = account_no
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_new_name(self, new_name):
        self.__name = new_name



    def get_bank_name(self):
        return self.__bank_name

    def set_new_bank_name(self, new_bank_name):
        self.__bank_name = new_bank_name



    def get_account_no(self):
        return self.__account_no

    def set_new_account(self, new_account):
        self.__account_no = new_account



    def get_balance(self):
        return self.__balance

    def set_new_balance(self, new_balance):
        self.__balance = new_balance

Acc1 = Bank_Account("shree", "SBI", 776998500, 1000000)
print(Acc1.get_name())
Acc1.set_new_name("raju")
print(Acc1.get_name())


print(Acc1.get_bank_name())
Acc1.set_new_bank_name("HDFC")
print(Acc1.get_bank_name())


print(Acc1.get_account_no())
Acc1.set_new_account(9922897035)
print(Acc1.get_account_no())


print(Acc1.get_balance())
Acc1.set_new_balance(300000)
print(Acc1.get_balance())