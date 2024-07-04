from BankAccount import BankAccount
class Account:
    
    def __init__(self, username: str, password: str, name: str,age: int) -> None:
        self.username =username
        self.password = password
        self.name= name
        self.age= age
        self.bank_accounts = list()
        
    def get_bank_accounts(self) -> list:
        return self.bank_accounts
    
    def get_ids_of_bank_account(self) -> list:
        if len(self.bank_accounts) == 0:
            return None
        ids: list = list()
        for bank_account in self.bank_accounts:
            id = bank_account.get_bank_account_id()
            ids.append(id)
        return ids
        
    def add_bank_account(self,bank_account_id: int, ammount: float) -> BankAccount:
        bank_account = BankAccount(bank_account_id,self.name,ammount)
        self.bank_accounts.append(bank_account)
        return self.bank_accounts[len(self.bank_accounts)-1]
    
    def add_bank_account_using_class(self,bank_account: BankAccount):
        self.bank_accounts.append(bank_account)
    
    def remove_bank_account(self, account_id:int) -> BankAccount:
        for num in range(len(self.bank_accounts)):
            if self.bank_accounts[num].get_bank_account_id() == account_id:
               return self.bank_accounts.pop(num) 
        return None
    
    def change_name(self,name:str) -> str:
        self.name =name
        if len(self.bank_accounts)> 0:
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
    def get_password(self) -> str:
        return self.password
    def get_name(self) -> str:
        return self.name
    def get_age(self) -> int:
        return self.age
    
    def __str__(self) -> str:
        collection = f"Account:\nName:{self.name}\nAge: {self.age}\n"
        if len(self.bank_accounts)> 0:
            for element in self.bank_accounts:
                collection += element.__str__() + "\n"
        return collection