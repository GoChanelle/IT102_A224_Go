class Account:
    # TODO 1: Create the constructor.
    def __init__(self, name, starting_balance):
        # TODO 2: Store the account name.
        self.account_name = name
        # TODO 3: Store the starting balance as an internal attribute.
        self._balance = starting_balance
 
    # TODO 4: Create check_balance().     
    def check_balance(self):
        return self._balace
 
    # TODO 5: Create deposit(). 
    def deposit(self, amount):
        if amount> 0:
            self._balance += amount
            return True
        return False
 
    # TODO 6: Create withdraw().
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False

""" 
######### Learning Signature ######### 
Programmed by: Clyde Balaman
Date Submitted: September 4, 2026
 
Program Description: This program is an updated version of Account from practice 8 that adds a withdraw option.
Reflection: I learned how to create object attributes and manage their values within a class.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""   
 
