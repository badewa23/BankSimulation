from Menu import Menu as M
import FileHandler as FH
from Bank import Bank as B
""" bank: Bank = Bank("Chase")
bank.add_account("bob","1234","Oluwatobi Olukunle",18)
account:Account = bank.accounts[0]
class_name = bank.__class__.__name__
dictionary = {bank.name:{account.username:{"Password": account.password,"Name": account.name,"Age": account.age}}} 
json_object = json.dumps(dictionary, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object) """
menu = M()
menu.start_up()


    
