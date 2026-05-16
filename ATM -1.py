class PassError(Exception):
    pass
class ATM:
    def user(self):
        self.password=2608
        try:
            Cus_pass=int(input("Enter your 4 digit Pin: "))
            if Cus_pass!=self.password:
                raise PassError
            print("---Sucessfully Login---")
            return True
        except PassError:
           print("Incorrect Pin! Please Enter Correct Pin")
           return False
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self):
        amount=int(input("Enter your Deposit Amount: "))
        self.balance=amount+self.balance
        print("Deposit Succesfully...")
    def withdraw(self):
        amount=int(input("Enter your withdraw Amount: "))
        if amount>self.balance:
            print("insufficinet balance")
        else:
            self.balance=self.balance-amount
            print("Withdraw Successfully...")
    def check_balance(self):
        print(f'Current Balance:{self.balance}')

def main():
    atm=ATM(50000)
    atm.user()
    while True:
        print("=== ATM MENU ===")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. EXIT")
        choice=int(input("Enter your Choice: "))
        if choice==1:
            atm.check_balance()
        elif choice==2:
            atm.deposit()
        elif choice==3:
            atm.withdraw()
        elif choice==4:
            print("..Thank You for Using ATM..")
            break
        else:
            print("invalid Choice")
        
main()
