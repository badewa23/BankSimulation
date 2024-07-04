from Account import Account
class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts = list()
    
    def get_bank_name(self) -> str:
        return self.name
    
    def get_accounts(self) -> str:
        return self.accounts
    
    def generate_account_id(self) -> int:
        if len(self.accounts) == 0:
            return 0
        else:
            ids = list()
            for account in self.accounts:
                list_of_id = account.get_ids_of_bank_account()
                if list_of_id is not None:
                    ids.extend(list_of_id)
            for num in range(len(ids)):
                if num not in ids:
                    return num
            return len(ids)
        
    def duplicate_username(self, username: str) -> bool:
        if len(self.accounts) > 0:
            for element in self.accounts:
                if element.get_username() == username:
                    return True
        else:
            return False
    
    def validate_login(self,username: str, password: str) -> Account:
        if len(self.accounts) > 0:
            for element in self.accounts:
               if element.validate_login(username, password):
                   return element
        return None
        
    def add_account(self, username: str, password: str, name: str, age: int) -> Account:
        account: Account = Account(username, password,name, age)
        if len(self.accounts) > 0:
            if self.duplicate_username(username):
                    return None
            self.accounts.append(account)
        else:
            self.accounts.append(account)
        for element in self.accounts:
                if element.get_username() == account.get_username():
                    return element
                
    def add_account_using_Account(self, account: Account) -> None:
        self.accounts.append(account)