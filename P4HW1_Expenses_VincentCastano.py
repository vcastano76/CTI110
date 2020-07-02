# CTI-110
# P4HW1 - Expenses
# Vincent Castano
# Created on July 2, 2020
# The program will prompt the user to enter the amount in the account
# in which money will be withdrawn from. The user will be prompted
# to enter the first line of expense which will be subtracted from the account.
# The user will be asked if he or she want to enter another expense.
# The user will find out the amount in the account after expenses are subtracted.

class Expense_Calculator: 
    def __init__(self): 
        self.balance=0
          
    def deposit(self): 
        amount=float(input("Enter starting amount in account: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter Expense 1: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ")

    def expense_ask(self):
        add_expense = input('Add expense? [y/n]: ')
        return add_expense
               
    def display(self): 
        print("\n Amount in accout AFTER expense subtracted is=",self.balance) 
  
  
# creating an object of class 
s = Expense_Calculator() 
   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 
s.expense_ask()
