from Bank import Bank
from Account import Account
from BankAccount import BankAccount
import json

def load_file() -> dict: 
    with open('data.json', 'r') as openfile:
        # Reading from json file
        data = json.load(openfile)
    return data
    
def save_file(data: dict) -> None:
    json_object = json.dumps(data, indent=3)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)

def create_bank(data: dict, bank_name: str):
    bank: Bank = Bank(bank_name)
    if data == {}:
        return bank
    else:
        for username in data:
            account_record = data[username]
            bank.add_account_using_Account(create_account(account_record, username))
        return bank
       
def create_account(data: dict, username) -> Account:
    user_info = data["Info"]
    password: str = user_info["Password"]
    name: str = user_info["Name"]
    age: int = int(user_info["Age"])
    account: Account = Account(username, password, name, age)
    account_record: list = data
    if len(account_record) == 1:
        return account
    elif len(account_record) > 1:    
        for bank_account_id in account_record:
            if bank_account_id.isdigit():
                id = int(bank_account_id)
                bank_account_record = data[bank_account_id]
                account.add_bank_account_using_bank_object(create_bank_acount(bank_account_record, id))
        return account
    else:
        print("An Error Occured")

def create_bank_acount(data: dict, id: int):
    name: str = data["Name"]
    balance: float = float(data["Ammount"])
    bank_account: BankAccount = BankAccount(id,name,balance)
    return bank_account
    
def save_banks(banks: list, data: dict) -> None:    
    if len(banks) > 0:
        for bank in banks:
            save_bank(bank, data)
            
def save_bank(bank: Bank, data: dict) -> None:
    name: str = bank.name
    accounts: list = bank.accounts
    data[name] = {}
    if len(accounts) > 0:
        for account in accounts:
            save_account(account, name, data)

def save_account(account: Account, bank_name: str, data: dict) -> None:
    username: str = account.username
    password: str = account.password
    user_name: str = account.name
    age: str = account.age
    data[bank_name][username] = {}
    data[bank_name][username]["Info"] = {"Password": password, "Name": user_name, "Age": age}
    bank_accounts: list = account.get_bank_accounts()
    if len(bank_accounts) > 0:
        for bank_account in bank_accounts:
            save_bank_account(bank_account, username, bank_name, data)

def save_bank_account(bank_account: BankAccount, username: str, bank_name: str, data: dict) -> None:
    bank_account_id: int = bank_account.account_id
    holder_name: str = bank_account.account_holder_name
    ammount: float = bank_account.ammount
    data[bank_name][username][bank_account_id] = {"Name": holder_name, "Ammount": ammount}