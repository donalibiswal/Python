class bankaccount:
    def set(self,bankname,branchname,ifsc,accountname,balance):
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

        
acc1=bankaccount()
acc2=bankaccount()
acc1.set("HDFC","bbsr",4567,"donali biswal",2500000)
acc2.set("SBI","BBSR",8976,"ANKITA PANDA",2900000)
acc1.display()
acc2.display()
        
