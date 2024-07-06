from BankAccount import BankAccount
class Account:
    
    def __init__(self, username: str, password: str, name: str,age: int) -> None:
        self.username =username
        self.password = password
        self.name= name
        self.age = age
        self.bank_accounts = list()
        self.ids = list()
        
    def get_bank_accounts(self) -> list:
        return self.bank_accounts
        
    def add_bank_account(self,bank_account_id: int, ammount: float) -> BankAccount:
        bank_account = BankAccount(bank_account_id,self.name,ammount)
        self.bank_accounts.append(bank_account)
        self.ids.append(self.bank_accounts[-1].get_bank_account_id())
        return self.bank_accounts[len(self.bank_accounts)-1]
    
    def get_ids(self) -> list:
        return self.ids
    
    def add_bank_account_using_bank_object(self,bank_account: BankAccount) -> None: 
        self.bank_accounts.append(bank_account)
        self.ids.append(self.bank_accounts[-1].get_bank_account_id())
    
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
    
    def change_password(self, old_password: str, password: str) -> int:
        if old_password == self.password:
            if password == self.password:
                return -2
            else:
                self.password = password
                return 0
        return -1
    
    def validate_login(self, username: str, password: str) -> bool:
        if username == self.username and password == self.password:
            return True
        return False
    
    def get_username(self) -> str:
        return self.username
    
    def change_age(self, age: int) -> bool:
        if age < 18:
            return False
        self.age = age
        return True
    
    def __str__(self) -> str:
        collection: str = f"Account:\nName:{self.name}\nAge: {self.age}\n"
        sum: float = 0
        count: int = 0
        if len(self.bank_accounts)> 0:
            for element in self.bank_accounts:
                sum += element.show_balance()
                count += 1
        collection += f"You have a total of $%.2f in {count} bank account"%sum
        return collection