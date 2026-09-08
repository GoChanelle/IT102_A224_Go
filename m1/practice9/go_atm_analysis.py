def analyze_transactions():
    # TODO 1: Try to open transactions.txt. Read all lines from the file.
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
 
    # TODO 2: If the file does not exist, return a dictionary containing zero or "None" values for the required analysis results.
    except FileNotFoundError:
        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0,
            "total_withdrawn": 0,
            "average_transaction": 0,
            "latest_transaction": "None",
            "latest_timestamp": "None",
            "largest_transaction": 0
        }

    # TODO 3: Create an empty list named transactions.
    transactions = []
 
    # TODO 4: Create an empty dictionary named current. This dictionary will temporarily store one transaction.
    current = {}
     
    # TODO 5: Use a for loop to process every line. TODO 6: Remove unnecessary spaces and newline characters.
    for line in lines:
        line = line.strip()
 
    # TODO 7: Ignore empty lines.
        if not line:
            continue
 
        if line.startswith("Timestamp:"):
            current["timestamp"] = (line.replace("Timestamp:", "").strip())

        elif line.startswith("Account:"):
            current["account"] = (line.replace("Account:", "").strip())

        elif line.startswith("Transaction:"):
            current["type"] = (line.replace("Transaction:", "").strip())

        elif line.startswith("Amount:"):

            try:
                current["amount"] = float(amount_text)
            except ValueError:
                current["amount"] = 0.0
 
    # TODO 12:
    # Once the required transaction
    # information has been collected,
    # add the transaction to the
    # transactions list.
    if "type" in current and "amount" in current:
        transactions.append(current.copy())
        current = {}
    
 
    # TODO 13: Calculate the total number of transactions.
    total_transactions = len(transactions)

 
    # TODO 14: Count the number of deposits.
    deposits = 0
 
    # TODO 15: Count the number of withdrawals.
    withdrawals = 0
 
    # TODO 16: Calculate the total amount deposited.
    total_deposited = 0
 
    # TODO 17: Calculate the total amount withdrawn.
    total_withdrawn = 0
 
    # TODO 18: Determine the largest transaction.
    largest_transaction = 0
 
    # TODO 19: Determine the latest transaction type.
    latest_transaction = "None"
 
    # TODO 20: Determine the latest timestamp.
    latest_timestamp = "None"

    for transaction in transactions:

        transaction_type = transaction["type"]
        amount = transaction["amount"]

        # Count deposits
        if transaction_type == "Deposit":

            deposits += 1
            total_deposited += amount

        # Count withdrawals
        elif transaction_type == "Withdraw":

            withdrawals += 1
            total_withdrawn += amount


        # Find largest transaction
        if amount > largest_transaction:

            largest_transaction = amount


        # Get latest transaction
        latest_transaction = transaction_type

        # Timestamp may not exist in old records
        if "timestamp" in transaction:

            latest_timestamp = transaction["timestamp"]
 
    # TODO 21: Calculate the average transaction amount. Avoid division by zero.
    if total_transactions > 0:

        total_amount = (
            total_deposited +
            total_withdrawn
        )

        average_transaction = (
            total_amount / total_transactions
        )

    else:

        average_transaction = 0
 
    # TODO 22: Return all calculated results inside one dictionary.
    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "latest_timestamp": latest_timestamp,
        "largest_transaction": largest_transaction
    }
""" 
######### Learning Signature ######### 
Programmed by: Chanelle Go
Date Submitted: September 8, 2026
 
Program Description: This program is the analysis module for an ATM. It gets the transaction data from a text file and calculates and summarizes the data.
Reflection: I learned how to analyze transaction data and calculate various metrics.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""
 
