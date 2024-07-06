from Account import Account
class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts = list()
        self.username_of_accounts = list ()
    
    def get_bank_name(self) -> str:
        return self.name
    
    def generate_account_id(self) -> int:
        if len(self.accounts) == 0:
            return 0
        else:
            ids = list()
            for account in self.accounts:
                list_of_id = account.get_ids()
                if len(list_of_id) > 0:
                    ids.extend(list_of_id)
            for num in range(len(ids)):
                if num not in ids:
                    return num
            return len(ids)
        
    def duplicate_username(self, username: str) -> bool:
        check = username in self.username_of_accounts
        return check
    
    def validate_login(self,username: str, password: str) -> Account:
        if len(self.accounts) > 0:
            for element in self.accounts:
               if element.validate_login(username, password):
                    return element
        return None
        
    def add_account(self, username: str, password: str, name: str, age: int) -> Account:
        account: Account = Account(username, password,name, age)
        if len(self.username_of_accounts) > 0:
            if username in self.username_of_accounts:
                    return None
            self.accounts.append(account)
            account =  self.accounts[-1]
            self.username_of_accounts.append(account.username)
        else:
            self.accounts.append(account)
            account =  self.accounts[-1]
            self.username_of_accounts.append(account.username)
            
        for element in self.accounts:
                if element.get_username() == account.get_username():
                    return element
                
    def add_account_using_Account(self, account: Account) -> None:
        self.accounts.append(account)
        account =  self.accounts[-1]
        self.username_of_accounts.append(account.username)