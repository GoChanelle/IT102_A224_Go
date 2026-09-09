# TODO 1: Import datetime.
from datetime import datetime

# TODO 2: Create withdraw_money().
def withdraw_money(account, amount):
    if amount <= 0:
        return False
    
    # TODO 4: Call the Account object's withdraw() method.
    success = account.withdraw(amount)

    # TODO 5: If successful, create a timestamp.
    if success:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # TODO 6: Open transactions.txt using append mode.
        with open("transactions.txt", "a") as file:

            # TODO 7: Write the timestamp.
            file.write(f"Timestamp: {timestamp}\n")
            # TODO 8: Write the account name.
            file.write(f"Account: {account.account_name}\n")
            # TODO 9: Write: Transaction: Withdraw
            file.write("Transaction: Withdraw\n")
            # TODO 10: Write the withdrawal amount.
            file.write(f"Amount: ₱{amount:.2f}\n\n")

        # TODO 11: Return True for a successful withdrawal.
        return True

    # TODO 12: Return False when the withdrawal fails.
    return False

""" 
######### Learning Signature ######### 
Programmed by: Chanelle Go
Date Submitted: September 2, 2026
 
Program Description: 
This program calls Account.withdraw() to withdraw money from an account. If the withdrawal is successful, it creates a timestamp and writes the transaction details to a text file.
Reflection: I learned how to use the datetime module to create timestamps.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""   
