class BankAccount:
    def __init__(self, account_id: int, account_holder_name: str, ammount: float) -> None:
        self.account_id= account_id
        self.account_holder_name = account_holder_name
        self.ammount = ammount
    def withdrawal(self,ammount: int) -> float:
        if(ammount <= self.ammount):
            self.ammount-= ammount
            return self.ammount
        else:
            return -1
    def deposit(self, ammount: int) -> float:
        self.ammount+= ammount
        return self.ammount
    def show_balance(self) -> float:
        return self.ammount
    def get_bank_account_id(self):
        return self.account_id
    def change_account_holder_name(self, name: str) -> str:
        self.account_holder_name = name
    def __str__(self) -> str:
        return f"{self.account_holder_name} has a balance of $%.2f"%self.ammount
        