from BankAccount import BankAccount
class Account:
    #Constructor
    def __init__(self, username: str, password: str, name: str,age: int):
        """ Creating Account object using arguments with no default value
        
            Parameters:
            username (str): Username of account must be unique
            password (str): Password of account
            name (str): Name of account only accept first_name and last_name
            age (int): Age of account must be over 18
            
            Returns:"""
        self.username =username
        self.password = password
        self.name= name
        self.age = age
        self.bank_accounts = list()
        self.ids = list()
    #Get list of BankAccount object from Account object
    def get_bank_accounts(self) -> list:
        """ Get list of BankAccount object from Account object
        
            Parameters:
                       
            Returns:
            list: List of BankAccount object"""
        return self.bank_accounts
    #Creating BankAccount object for Account object  
    def add_bank_account(self,bank_account_id: int, ammount: float) -> BankAccount:
        """ Creating BankAccount object for Account object
        
            Parameters:
            bank_account_id (int): Bank account id
            ammount (float): Balance of bank account
            
            Returns:
            BankAccount: BankAccount object from the last postion of the list of BankAccount objects"""
        bank_account = BankAccount(bank_account_id,self.name,ammount)
        self.bank_accounts.append(bank_account)
        self.ids.append(self.bank_accounts[-1].get_bank_account_id())
        return self.bank_accounts[len(self.bank_accounts)-1]
    #Get list of BankAccoint ids from Account object
    def get_ids(self) -> list:
        """ Get list of BankAccoint ids from Account object
        
            Parameters:
                       
            Returns:
            list: List of bank account ids"""
        return self.ids
    #Add a BankAccount object to Account object
    def add_bank_account_using_object(self,bank_account: BankAccount):
        """ Add a BankAccount object to Account object
        
            Parameters:
            bank_account (BankAccount): BankAccount object
            
            Returns:""" 
        self.bank_accounts.append(bank_account)
        self.ids.append(self.bank_accounts[-1].get_bank_account_id())
    #Change name information of the Account object
    def change_name(self,name:str) -> str:
        """ Change name information of the Account object
        
            Parameters:
            name (str): BankAccount object
            
            Returns:
            str: Name of Account object""" 
        self.name =name
        if len(self.bank_accounts)> 0:
            for element in self.bank_accounts:
                element.change_account_holder_name(self.name)
        return self.name
    #Change password information of Account object
    def change_password(self, old_password: str, password: str) -> int:
        """ Change password information of Account object
        
            Parameters:
            old_password (str): Old password of this Account object
            password (str): New password to add to this Account object
            
            Returns:
            int: Status code, -1 for wrong old password, -2 for new password same as old password,
            0 for successful change of password"""
        if old_password == self.password:
            if password == self.password:
                return -2
            else:
                self.password = password
                return 0
        return -1
    #Check for if username and password given belong to the Account object
    def validate_login(self, username: str, password: str) -> bool:
        """ Check for if username and password given belong to the Account object
        
            Parameters:
            username (str): Username input
            password (str): Password input
            
            Returns:
            bool: True if username and password input same as Account object username and password"""
        if username == self.username and password == self.password:
            return True
        return False
    #Get username information from Account object 
    def get_username(self) -> str:
        """ Get username information from Account object
        
            Parameters:
                       
            Returns:
            str: Username information of Account object"""
        return self.username
    #Change age information of Account object
    def change_age(self, age: int) -> bool:
        """ Change age information of Account object
        
            Parameters:
            age (int): age input
            
            Returns:
            bool: True if age is over or equal to 18"""
        if age < 18:
            return False
        self.age = age
        return True
    #Give the string information of Account object
    def __str__(self) -> str:
        """ Give the string information of Account object
        
            Parameters:
                       
            Returns:
            str: Username, age, list of BankAccount object information of Account object"""
        collection: str = f"Account:\nName:{self.name}\nAge: {self.age}\n"
        sum: float = 0
        count: int = 0
        if len(self.bank_accounts)> 0:
            for element in self.bank_accounts:
                sum += element.show_balance()
                count += 1
        collection += f"You have a total of $%.2f in {count} bank account"%sum
        return collection