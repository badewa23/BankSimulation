from BankAccount import BankAccount
from Account import Account
from Bank import Bank
import FileHandler as FH

class Menu:
    def __init__(self, data: dict = dict(), banks: list = list()) :
        self.data = FH.load_file()
        self.banks = self.get_bank_record()
    
    def save(self) -> None:
        FH.save_file(self.data)   
        
    def get_bank_record(self) ->list:
        banks: list = list()
        for bank_name in self.data:
            bank_record: dict = self.data[bank_name]
            banks.append(FH.create_bank(bank_record, bank_name))
        return banks
    
    def start_up(self) -> None:
        self.banks_menu()
        
    def banks_menu(self) -> None:
        print(f"Welcome to Bank Simulation\n")
        banks: list = self.banks
        while True:
            print("Banks Available:")
            for num in range(len(banks)):
                name: str = banks[num].get_bank_name()
                print(f"{name} [{num}]")
            print("[E]xit")
            selection : str = input()
            if selection.isdigit():
                selection: int = int(selection)
                if selection in range(len(banks)):
                    self.bank_menu(banks[selection])
                else:
                    print(f"{selection} is not a choice")
                    continue
            else:
                if selection != "E":
                    print("Wrong input please try again")
                else:
                    self.save()
                    exit()
                
    def bank_menu(self, bank: Bank) -> None:
        while True:
            print(f"Welcome To {bank.name} Bank")
            selection: str = input("[L]ogin\n[C]reate Account\n[E]xit\n[G]0 Back\n")
            if selection not in "GELC" or len(selection) != 1:
                print("Wrong input please try again")
                continue
            match selection:
                case "G":
                    self.banks_menu()
                case "E": 
                    self.save()  
                    exit()
                case "L":    
                    username: str = input("Username: ")
                    passowrd: str = input("Password: ")
                    account: Account = bank.validate_login(username, passowrd)
                    if account is not None:
                        self.account_Menu(account, bank)
                    else:
                        print("Wrong Username Or Password")
                        continue
                case "C":
                    while True:
                        print("Creating Account:") 
                        while True:   
                            username: str = input("Username: ")
                            if bank.duplicate_username(username):
                                print("Duplicate Username")
                                continue
                            else:
                                break
                        passowrd: str = input("Password: ")
                        while True:
                            name: str = input("Name: ")
                            if any(i.isdigit() for i in name):
                                print("Please Only Input in Alphabet")
                                continue
                            else:
                                if len(name.split()) > 2 or len(name.split()) < 2:
                                    print("Please Only Input A First Name And Last Name")
                                    continue
                                else:
                                    break
                        while True:
                            age: str = input("Age: ")
                            if age.isdigit():
                                age: int = int(age)
                                if age >= 18:
                                    break
                                else:
                                    print("Must be older than 18")  
                                    self.bank_menu(bank)
                            else:
                                print("Please Only Input Digit")
                                continue
                        if int(age )< 18:
                            break
                        bank.add_account(username,passowrd,name,age)
                        account = bank.validate_login(username,passowrd)
                        if account is not None:
                            FH.save_account(account, bank.name, self.data)
                            self.account_Menu(account, bank)
                        else:
                            print("Mistake was made")
                            continue
                    
    def account_Menu(self, account: Account, bank: Bank) -> None:
        while True:
            print(f"{account.username} Account:")
            selection: str = input("[G]o Back\n[B]ank Accounts\n[C]reate Bank Account\n[E]exit\n")
            if selection not in "EGCB" or len(selection) != 1:
                print("Wrong input please try again")
                continue
            match selection:
                case "E":
                    self.save()   
                    exit()
                case "G":
                    self.bank_menu(bank)
                    break
                case "C":
                    while True:
                        ammount: str = input("How Much Are You Opening The Bank Account With\n")
                        if ammount.isdigit():
                            ammount: float = float(ammount)
                            serial: int = bank.generate_account_id()
                            bank_account = account.add_bank_account(serial, ammount)
                            FH.save_bank_account(bank_account,account.username,bank.name,self.data)
                            break
                        else:
                            print("Only Input Digits Please")
                            continue
                case "B":
                    bank_accounts = account.bank_accounts
                    if len(bank_accounts) > 0:
                        while True:
                            print("Which Bank Account Do You Want Choose:\n")
                            for num in range(len(bank_accounts)):
                                id: int = bank_accounts[num].get_bank_account_id()
                                balance: float = bank_accounts[num].show_balance()
                                print(f"{id} has a balance of $%.2f [{num}]"%balance)
                            choice: str = input()
                            if choice.isdigit():
                                choice: int = int(choice)
                                if choice in range(len(bank_accounts)):
                                    self.bank_account_holder_menu(bank_accounts[choice], account, bank) 
                                    break                      
                                else:
                                    print(f"{choice} Is Not Among The Choice, Try Again")
                                    continue
                            else:
                                print("Only Input Digits Please")
                                continue
                    elif len(bank_accounts)== 1:
                        bank_account: BankAccount = bank_accounts[0]
                        self.bank_account_holder_menu(bank_account, account, bank)
                        break
                    else:
                        print("You Don't Have A Bank Account, Please Create One")
                    

    def bank_account_holder_menu(self, bank_account: BankAccount, account: Account, bank: Bank) -> None:
        while True:
            print(f"Welcome {bank_account.account_holder_name} what would you like to "
                + "do today\n[W]ithdrawal\n[D]eposit\n[B]alance\n[E]xit\n[G]o back")
            selection: str = input()
            if selection not in "WDBEG" or len(selection) != 1:
                print("Wrong input please try again")
                continue
            match selection:
                case "G":
                    self.account_Menu(account, bank)
                    break
                case "E":
                    self.save()
                    exit()
                case "B":
                    print(f"You Have $%.2f In Your Account"%bank_account.show_balance())
                case "D":
                    while True:
                        ammount: str = input("How Much Do You Want To Deposit\n")
                        if ammount.isdigit():
                            bank_account.deposit(float(ammount))
                            FH.save_bank_account(bank_account,account.username,bank.name,self.data)
                            print("Thank You For The Deposit")
                            print(f"Your New Balance is $%.2f"%bank_account.show_balance())
                            break
                        else:    
                            print("Please Only Input In Digits, Try Again")
                            continue
                case "W":
                    while True:
                        ammount: str = input("How Much Do You Want To Withdrwal\n")
                        if ammount.isdigit():
                            new_balance = bank_account.withdrawal(float(ammount))
                            if new_balance == -1:
                                print(f"$%.2f Will Cause You To OverDraft,"%float(ammount)
                                    + f" You Only Have $%.2f"% bank_account.show_balance() 
                                    + " Try Again!")
                                continue
                            else:
                                FH.save_bank_account(bank_account,account.username,bank.name,self.data)
                                print(f"Your New Balance is $%.2f"%new_balance)
                                break
                        else:
                            print("Please Only Input In Digits, Try Again")
                            continue