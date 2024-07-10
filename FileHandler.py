from Bank import Bank
from Account import Account
from BankAccount import BankAccount
import json
#Import dictionary data from file
def load_file(file_name: str) -> dict:
    """ Import dictionary data from file
        
            Parameters:
            file_name (str): Json file path
            
            Returns:
            ditc: Json data as dictionary data""" 
    with open(file_name, 'r') as openfile:
        # Reading from json file
        data = json.load(openfile)
    return data
#Export dictionary data to file     
def save_file(data: dict, file_name):
    """ Export dictionary data to file  
        
            Parameters:
            data (ditc): Dictionary data from program 
            file_name (str): Json file path
            
            Returns:""" 
    json_object = json.dumps(data, indent=3)
    with open(file_name, "w") as outfile:
        outfile.write(json_object)
#Create Bank object from dictionary data
def create_bank(data: dict, bank_name: str) -> Bank:
    """ Create Bank object from dictionary data  
        
            Parameters:
            data (ditc): Dictionary to create objects
            bank_name (str): Bank's name
            
            Returns:
            Bank: Bank object created form dictionary data""" 
    bank: Bank = Bank(bank_name)
    if data == {}:
        return bank
    else:
        for username in data:
            account_record = data[username]
            bank.add_account_using_Account(create_account(account_record, username))
        return bank
#Create Account object from dictionary data       
def create_account(data: dict, username: str) -> Account:
    """ Create Account object from dictionary data  
        
            Parameters:
            data (ditc): Dictionary to create objects
            username (str): Username of account
            
            Returns:
            Account: Account object created form dictionary data""" 
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
                account.add_bank_account_using_object(create_bank_acount(bank_account_record, id))
        return account
    #For Error Checking
    else:
        print("An Error Occured")
#Create BankAccount object from dictionary data
def create_bank_acount(data: dict, id: int):
    """ Create BankAccount object from dictionary data  
        
            Parameters:
            data (ditc): Dictionary to create objects
            id (int): Bank account id
            
            Returns:
            BankAccount: BankAccount object created form dictionary data""" 
    name: str = data["Name"]
    balance: float = float(data["Ammount"])
    bank_account: BankAccount = BankAccount(id,name,balance)
    return bank_account
#Add list of Bank object information to dictionary data    
def save_banks(banks: list, data: dict):
    """ Add list of Bank object information to dictionary data  
        
            Parameters:
            banks (list): List of bank object
            data (ditc): Dictionary data from file 
            
            Returns:"""     
    if len(banks) > 0:
        for bank in banks:
            save_bank(bank, data)
#Add Bank object information to dictionary data            
def save_bank(bank: Bank, data: dict):
    """ Add Bank object information to dictionary data  
        
            Parameters:
            banks (Bank): bank object
            data (ditc): Dictionary data from file 
            
            Returns:"""
    name: str = bank.name
    accounts: list = bank.accounts
    data[name] = {}
    if len(accounts) > 0:
        for account in accounts:
            save_account(account, name, data)
#Add Account object information to dictionary data
def save_account(account: Account, bank_name: str, data: dict):
    """ Add Bank object information to dictionary data  
        
            Parameters:
            account (Account): Account object
            bank_name (str): Name of bank for account
            data (ditc): Dictionary data from file 
            
            Returns:"""
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
#Add BankAccount object information to dictionary data
def save_bank_account(bank_account: BankAccount, username: str, bank_name: str, data: dict):
    """ Add BankAccount object information to dictionary data  
        
            Parameters:
            bank_account (BankAccount): BankAccount object
            username (str): Username of account for bank account
            bank_name (str): Name of bank for bank account
            data (ditc): Dictionary data from file 
            
            Returns:"""
    bank_account_id: int = bank_account.account_id
    holder_name: str = bank_account.account_holder_name
    ammount: float = bank_account.balance
    data[bank_name][username][bank_account_id] = {"Name": holder_name, "Ammount": ammount}