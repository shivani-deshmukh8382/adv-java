class Customer:
    
    bankName='HDFC Bank'
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def deposite(self,amount):
        self.balance=self.balance+amount
        print('you have deposited :',amount)
        print('your total balance is :',self.balance)
        
    def withdrow(self,amount):
        if(self.balance<amount):
            print("Insufficient balance in your account")
            
        else:
            self.balance=self.balance-amount
            print("Balance after withdrowing...",self.balance)
            
#cust = Customer('shivani',10000)
cust2=Customer('Ashish',20000)
#cust.withdrow(2000)
cust2.deposite(5000)
cust2.withdrow(30000)
cust2.withdrow(20000)