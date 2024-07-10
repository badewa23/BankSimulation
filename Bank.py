from Account import Account
class Bank:
    #Constructor
    def __init__(self, name: str):
        """ Create Bank object using an argument with no default value
        
            Parameters:
            name (str): Name of bank
            
            Returns:"""
        self.name = name
        self.accounts = list()
        self.username_of_accounts = list ()
    #Get name information from Bank object
    def get_bank_name(self) -> str:
        """ Get name information from Bank object
        
            Parameters:
                       
            Returns:
            str: Name information of Bank object"""
        return self.name
    #Create unique bank account id 
    def generate_account_id(self) -> int:
        """ Create unique bank account id
        
            Parameters:
                       
            Returns:
            int: The generated id"""
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
    #Check if username exist already in Bank object  
    def duplicate_username(self, username: str) -> bool:
        """ Check if username exist already in Bank object
        
            Parameters:
            username (str): Username input
            
            Returns:
            bool: True if username already exist in the list of username else False"""
        return username in self.username_of_accounts
    #Check if the right combination of username and password exist in Bank object
    def validate_login(self,username: str, password: str) -> Account:
        """ Check if the right combination of username and password exist in Bank object
        
            Parameters:
            username (str): Username input
            password (str): Password input
            
            Returns:
            Account: The Account object of the username and password combination is returned if 
            No such combination exist return None"""
        if len(self.accounts) > 0:
            for element in self.accounts:
               if element.validate_login(username, password):
                    return element
        return None
    #Create Account object for Bank object   
    def add_account(self, username: str, password: str, name: str, age: int) -> Account:
        """ Creating Account object for Bank object
        
            Parameters:
            username (str): Username input must be unique
            password (str): Password input
            name (str): Name input only accept first_name and last_name
            age (int): Age input must be over 18
            
            Returns:
            Account: Account object from the last postion of the list of Account objects if duplicate
            returns None"""
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
    #Add an Account object to Bank object            
    def add_account_using_Account(self, account: Account):
        """ Add a Account object to Bank object
        
            Parameters:
            account (Account): Account object
            
            Returns:"""
        self.accounts.append(account)
        account =  self.accounts[-1]
        self.username_of_accounts.append(account.username)