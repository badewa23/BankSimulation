from Account import Account
class Bank:
    accounts: list = list()
    def __init__(self, name: str) -> None:
        self.name = name
    def duplicate_username(self, username: str) -> bool:
        if self.accounts.__len__() > 0:
            for element in self.accounts:
                if element.get_username() == username():
                    return True
        else:
            return False
    def add_account(self, username: str, password: str, age: int) -> Account:
        account: Account = Account(username, password, age)
        if self.accounts.__len__() > 0:
            for element in self.accounts:
                if element.get_username() == account.get_username():
                    return None
            self.accounts.append(account)
        else:
            self.accounts.append(account)
        for element in self.accounts:
                if element.get_username() == account.get_username():
                    return element
    def validate_login(self,username: str, password: str) -> Account:
        if self.accounts.__len__() > 0:
            for element in self.accounts:
               if element.validate_login(username, password):
                   return element
        return None