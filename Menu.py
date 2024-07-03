from BankAccount import BankAccount
from Account import Account
from Bank import Bank

serial: int =0

def bank_menu(bank: Bank) -> None:
    while True:
        print(f"Welcome To {bank.name} Bank")
        selection: str = input("[L]ogin\n[C]reate Account\n[E]xit\n")
        if selection not in "LCE" or selection.__len__() != 1:
            print("Wrong input please try again")
            continue
        match selection:
            case "E":   
                break
            case "L":    
                username: str = input("Username: ")
                passowrd: str = input("Password: ")
                account: Account = bank.validate_login(username, passowrd)
                if account is not None:
                    account_Menu(bank,account)
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
                            if name.split().__len__() > 2 or name.split().__len__() < 2:
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
                                bank_menu(bank)
                        else:
                            print("Please Only Input Digit")
                            continue
                    bank.add_account(username,passowrd,name,age)
                    account = bank.validate_login(username,passowrd)
                    if account is not None:
                        account_Menu(bank, account)
                    else:
                        print("Mistake was made")
                        continue
                
def account_Menu(bank: Bank, account: Account) -> None:
    while True:
        print(account)
        selection: str = input("[G]o Back\n[B]ank Accounts\n[C]reate Bank Account\n[E]exit")
        if selection not in "GBCE" or selection.__len__() != 1:
            print("Wrong input please try again")
            continue
        match selection:
            case "E":   
                    break
            case "G":
                bank_menu(bank)
            case "C":
                while True:
                    ammount: str = input("How Much Are You Opening The Bank Acount With\n")
                    if ammount.isdigit():
                        ammount: float = float(ammount)
                        account.add_bank_account(serial, ammount)
                        break
                    else:
                        print("Only Input Digits Please")
                        continue
            case "B":
                bank_accounts = account.bank_accounts
                if bank_accounts.__len__() > 0:
                    while True:
                        print("Which Bank Account Do You Want Choose:\n")
                        for num in (0, bank_accounts.__len__()):
                            id: int = bank_accounts[num].get_bank_account_id()
                            balance: float = bank_accounts[num].show_balance()
                            print(f"{id} has a balance of $%.2f [{num}]"%balance)
                        choice: str = input()
                        if choice.isdigit():
                            if choice in (0, bank_accounts.__len__()):
                                bank_account_holder_menu(bank_accounts[int(choice), account])                       
                            else:
                                print(f"{choice} Is Not Among The Choice, Try Again")
                                continue
                        else:
                            print("Only Input Digits Please")
                            continue
                elif bank_accounts.__len__() == 1:
                    account: Account = bank_accounts[0]
                    bank_account_holder_menu(account, account)
                else:
                    print("You Don't Have A Bank Account, Please Create One")
                

def bank_account_holder_menu(bank_account: BankAccount, account: Account) -> None:
    while True:
        print(f"Welcome {bank_account.account_holder_name} what would you like to "
              + "do today\n[W]ithdrawal\n[D]eposit\n[B]alance\n[E]xit\n[G]o back")
        selection: str = input()
        if selection not in "WDBEG" or selection.__len__() != 1:
            print("Wrong input please try again")
            continue
        match selection:
            case "G":
                 account_Menu(account)
            case "E":
                break
            case "B":
                print(f"You Have $%.2f In Your Account"%bank_account.show_balance())
            case "D":
                while True:
                    ammount: str = input("How Much Do You Want To Deposit\n")
                    if ammount.isdigit():
                        bank_account.deposit(float(ammount))
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
                            print(f"Your New Balance is $%.2f"%new_balance)
                            break
                    else:
                        print("Please Only Input In Digits, Try Again")
                        continue