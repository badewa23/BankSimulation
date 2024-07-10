class BankAccount:
    #Constructor
    def __init__(self, account_id: int, account_holder_name: str, ammount: float):
        """ Create BankAccount object using an arguments with no default value
        
            Parameters:
            account_holder_name (str): Name on bank account
            ammount (float): Balance on bank account
            
            Returns:"""
        self.account_id= account_id
        self.account_holder_name = account_holder_name
        self.balance = ammount
    #Subtract some ammount of money from BankAccount object    
    def withdrawal(self,ammount: float) -> float:
        """ Subtract some ammount of money from BankAccount object
        
            Parameters:
            ammount (float): Ammount to witdrawal from bank account
            
            Returns:
            flaot: The new balance is successful or else -1 if the withdrawal would make the balance
            negative"""
        if(ammount <= self.balance):
            self.balance-= ammount
            return self.balance
        else:
            return -1
    #Add some ammount of money to BankAccount object    
    def deposit(self, ammount: float) -> float:
        """ Add some ammount of money to BankAccount object
        
            Parameters:
            ammount (float): ammount to deposit from bank account
            
            Returns:
            flaot: New balance of BankAccount object"""
        self.balance+= ammount
        return self.balance
    #Get balance information form BankAccount object 
    def show_balance(self) -> float:
        """ Get balance information form BankAccount object
        
            Parameters:
            
            Returns:
            flaot: Balance of BankAccount object"""
        return self.balance
    #Get id form BankAccount object 
    def get_bank_account_id(self) -> int:
        """ Get id form BankAccount object
        
            Parameters:
            
            Returns:
            int: Bank account id of BankAccount object"""
        return self.account_id
    #Change name information of the BankAccount object
    def change_account_holder_name(self, name: str):
        """ Change name information of the BankAccount object
        
            Parameters:
            name (str): Name input
            
            Returns:"""
        self.account_holder_name = name
    #Give the string information of BankAccount object    
    def __str__(self) -> str:
        """ Give the string information of BankAccount object
        
            Parameters:
                       
            Returns:
            str: Name on account and the balance of bank account"""
        return f"{self.account_holder_name} has a balance of $%.2f"%self.balance
        