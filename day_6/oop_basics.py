"""
class: Student
variables: name,grade
methods: study
"""

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def study(self):
         print(f"{self.name} is studying {self.grade}")

"""
class: BankAccount
variables: initial_balance
methods: deposit,withdraw,viewBalance
"""

class BankAccount:
    def __init__(self,initial_balance):
        self.initial_balance = round(initial_balance,2)
        
    def view_balance(self):
        return self.initial_balance    

    def deposit(self,amount):
        self.initial_balance = round(self.initial_balance + amount,2)
        print(f"${amount} credited to your account.")
        print(self.view_balance())

    def withdraw(self,amount):
        if amount > self.view_balance():
            print("Insufficient Balance")
            return
        self.initial_balance = round(self.initial_balance - amount,2)
        print(f"${amount} debited from your account.")
        print(self.view_balance())



basic_amount = float(input("Enter basic amount to create bank account: "))
account = BankAccount(basic_amount)
        
while(True):
    print("1.Deposit\n2.Withdraw\n3.View_balance\n4.Exit")
    user_choice = int(input("Enter your choice:"))

    match user_choice:
        case 1:
            amount = float(input("Amount to deposit: "))
            account.deposit(amount)
        case 2:
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)
        case 3:
            print(f"The current balance is {account.view_balance()}")
        case 4:
            break
        case _:
            print("wrong choice")

name = input("Enter a name:")
grade = input("Enter a grade:")
student_1 = Student(name,grade)
student_1.study()
student_2 = Student(input("Enter a name:"), input("Enter a grade:"))
student_2.study()

            

    