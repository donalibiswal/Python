class BankAccount:
    pass
def __init__(self,bankname,branchname,ifsc,accountname,balance):
    self.bankname=bankname
    self.branchname=branchname
    self.ifsc=ifsc
    self.accountname=accountname
    self.balance=balance
    
def display(self):
    print("bankname is:",self.bankname)
    print("branchname is:",self.branchname)
    print("ifsc is:",self.ifsc)
    print("accountname is:",self.accountname)
    print("balance is:",self.balance)
account=BankAccount("SBI","bbsr",5678,"donali",5600000)
account.display()
