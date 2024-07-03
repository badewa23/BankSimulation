from BankAccount import BankAccount
class Account:
    bank_accounts: list = list()
    def __init__(self,username: str, password: str, name: str,age: int) -> None:
        self.username =username
        self.password = password
        self.name= name
        self.age= age
    def add_bank_account(self,bank_account_id: int, ammount: float) -> BankAccount:
        bank_account = BankAccount(bank_account_id,self.name,ammount)
        self.bank_accounts.append(bank_account)
        for element in self.bank_accounts:
            if(element.get_bank_account_id()):
                return element
        return None
    def remove_bank_account(self, account_id:int) -> BankAccount:
        for num in (0,self.bank_accounts.__len__()):
            if self.bank_accounts[num].get_bank_account_id() == account_id:
               return self.bank_accounts.pop(num) 
        return None
    def change_name(self,name:str) -> str:
        self.name =name
        if self.bank_accounts.__len__() > 0:
            for element in self.bank_accounts:
                element.change_account_holder_name(self.name)
        return self.name
    def change_password(self, password) -> int:
        if password == self.password:
            return -1
        self.password = password
        return 1
    def validate_login(self, username: str, password: str) -> bool:
        if username == self.username and password == self.password:
            return True
        return False
    def get_username(self) -> str:
        return self.username
    def __str__(self) -> str:
        collection = f"Account:\nName:{self.name}\nAge: {self.age}\n"
        if self.bank_accounts.__len__() > 0:
            for element in self.bank_accounts:
                collection += element.__str__() + "\n"
        return collection
    