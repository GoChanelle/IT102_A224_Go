import streamlit as st
 
from go_atm_account import Account
import go_atm_balance
import go_atm_deposit
import go_atm_withdraw
import go_atm_history
import go_atm_analysis
 
 
# TODO 7: Create the Account object.
account = Account("Chanelle Go", 10000.00)
  
# TODO 8: Configure the Streamlit page.
st.set_page_config(
  page_title="Python ATM",
  page_icon="🏦",
  layout="wide"
)
  
# TODO 9: Display the main ATM title.
st.title("PYTHON ATM")
  
# TODO 10: Display a welcome message using the account name.
st.write(f"Welcome, *{account.account_name}*!")
 
# TODO 11: Add a divider.
st.divider()
 
 
# TODO 12: Create the sidebar title.
st.sidebar.title("ATM MENU")
 
# TODO 13: Create a sidebar radio menu
choice = st.sidebar.radio(
  "Select an option:",
  [
    "Check Balance",
    "Deposit",
    "Withdraw",
    "View History",
    "Analyze Transactions",
  ]
)

# CHECK BALANCE HERE
# TODO 14: Check whether the selected option "Check Balance".
if choice == "Check Balance":
 
# TODO 15: Display a page header.
  st.header("Check Balance")
 
# TODO 16: Call the balance module and obtain the current account balance.
  balance = (go_atm_balance.check_balance(account))
 
# TODO 17: Display the balance using a Streamlit metric.
  st.metric(
    "Current Balance",
    f"P{balance:,.2f}"
    )

# DEPOSIT HERE
# TODO 18: Add the "Deposit" branch.
elif choice == "Deposit":
 
# TODO 19: Display the Deposit Money header.
  st.header("Deposit Money")
 
# TODO 20: Create a number input.
  amount = st.number_input(
    "Enter deposit amount",
    min_value=0.0,
    step=100.0,
    format="%.2f"
  ) 
 
# TODO 21: Create a button named: Deposit Money
  if st.button("Deposit Money"):
  
# TODO 22: When the button is clicked, check whether the amount is valid.
# TODO 23: If the amount is invalid, display a Streamlit error message. 
    if amount <= 0:
      st.error("Invalid deposit amount.")

# TODO 24: Otherwise, call the deposit module.  
    else:
      success = (
        go_atm_deposit.deposit_money(account, amount)
      )

# TODO 25: If the deposit is successful, display a success message.
      if success:
        st.success("Deposit Successful.")
 
# TODO 26: Display the updated balance using a Streamlit metric.
      st.metric(
        "New Balance",
        f"P{account.check_balance():,.2f}"
      )

# WITHDRAW HERE
# TODO 27: Add the "Withdraw" branch.
elif choice == "Withdraw": 
 
# TODO 28: Display the Withdraw Money header.
  st.header("Withdraw Money")
 
# TODO 29: Display the available account balance.
  st.write(
    f"Available Balance: "
    f"P{account.check_balance():,.2f}"
  ) 
 
# TODO 30: Create a number input for the withdrawal amount.
  amount = st.number_input(
    "Enter withdrawal amount",
    min_value=0.0,
    step=100.0,
    format="%.2f"
  )
 
# TODO 31: Create the Withdraw Money button.
  if st.button("Withdraw Money"):
 
# TODO 32: Check whether the withdrawal amount is valid.
    if amount <= 0:
 
 
# TODO 33: Display an error if the amount is zero or negative.
      st.error("Invalid withdrawal amount.")
 
# TODO 34: Check whether the requested amount is greater than the current balance.
    elif amount > account.check_balance():
 
# TODO 35: Display an error when the account has insufficient balance.
      st.error("Insufficient balance.")
 
# TODO 36: Call the withdrawal module when the amount is valid.
    else:
      success = (
        go_atm_withdraw.withdraw_money(account, amount)
      )
 
# TODO 37: Display a success message after a successful withdrawal.
      if success:
        st.success("Withdrawal successful.")
 
# TODO 38: Display the updated balance. 
        st.metric(
          "New Balance",
          f"P{account.check_balance():,.2f}"
        )

# HISTORY HERE
# TODO 39: Add the "View History" branch.
elif choice == "View History":
 
# TODO 40: Display the Transaction History header.
  st.header("Transaction History")
 
# TODO 41: Call view_history() from the history module.
  lines = (
    go_atm_history.view_history()
  )
 
# TODO 42: Create an empty list named transactions.
  transactions = []
 
# TODO 43: Create an empty dictionary for the current transaction.
  current_transaction = {}
 
# TODO 44: Use a for loop to process every returned line.
  for line in lines:
 
# TODO 45: Remove unnecessary spaces and newline characters.
    line = line.strip()
 
# TODO 46: Skip empty lines.
    if not line:
      continue
 
# TODO 47: Detect Timestamp lines.
    if line.startswith("Timestamp: "):
      current_transaction["Timestamp"] = (
        line.replace(
          "Timestamp:",
          ""
        ).strip()
      )
 
# TODO 48: Detect Account lines.
    elif line.startswith("Account: "):
      current_transaction["Account"] = (
        line.replace(
          "Account:",
          ""
        ).strip()
      )
 
# TODO 49: Detect Transaction lines.
    elif line.startswith("Transaction: "):
      current_transaction["Transaction"] = (
        line.replace(
          "Transaction:",
          ""
        ).strip()
      )
 
# TODO 50: Detect Amount lines.
    elif line.startswith("Amount: "):
      current_transaction["Amount"] = (
        line.replace(
          "Amount: P",
          ""
        ).strip()
      )
 
# TODO 51: Add completed transactions to the transactions list.
      transactions.append(current_transaction)
      current_transaction = {}
 
# TODO 52: Display the transactions using an appropriate Streamlit table component.
  if transactions:

        st.dataframe(
            transactions,
            use_container_width=True,
            hide_index=True
        )
 
# TODO 53: If there are no transactions, display an informational message.
  else:

        st.info(
            "No transactions available."
        )

# ANALYSIS HERE
# TODO 54: Add the "Analyze Transactions" branch.
elif choice == "Analyze Transactions":
 
# TODO 55: Display the Transaction Analysis header.
  st.header("Transaction Analysis")
 
# TODO 56: Call analyze_transactions()
  result = (
    go_atm_analysis.analyze_transactions()
  )
 
 
# ==========================================
# TRANSACTION SUMMARY
# ==========================================
 
# TODO 57: Display: Transaction Summary
  st.subheader("1. Transaction Summary")
 
 
# TODO 58: Create three Streamlit columns.
  col1, col2, col3 = st.columns(3)
 
 
# TODO 59: Display: Total Transactions
  col1.metric(
    "Total Transactions",
    result["total_transactions"]
  )
 
 
# TODO 60: Display: Deposits
  col2.metric(
    "Deposits",
    result["deposits"]
  )
 
# TODO 61: Display: Withdrawals
  col3.metric(
    "Withdrawals",
    result["withdrawals"]
  )
 
# ==========================================
# TRANSACTION AMOUNT ANALYSIS
# ==========================================
 
# TODO 62: Add a divider.
  st.divider()
 
# TODO 63: Display:
# 2. Transaction Amount Analysis
  st.subheader(
      "2. Transaction Amount Analysis"
    )
 
# TODO 64: Create three columns.
  col1, col2, col3 = st.columns(3)
 
# TODO 65: Display: Total Deposited
  col1.metric(
    "Total Deposited",
    f"₱{result['total_deposited']:,.2f}"
  ) 
 
# TODO 66: Display: Total Withdrawn
  col2.metric(
    "Total Withdrawn",
    f"₱{result['total_withdrawn']:,.2f}"
  ) 
 
# TODO 67: Display: Average Transaction
  col3.metric(
    "Average Transaction",
    f"₱{result['average_transaction']:,.2f}"
  )
 
# ==========================================
# ACCOUNT ACTIVITY ANALYSIS
# ==========================================
 
 
# TODO 68: Add another divider.
  st.divider()
 
# TODO 69: Display:
# 3. Account Activity Analysis
  st.subheader(
    "3. Account Activity Analysis"
  )
 
# TODO 70: Create three columns.
  col1, col2, col3 = st.columns(3)
 
 
# TODO 71: Display: Latest Transaction
  col1.metric(
    "Latest Transaction",
    result["latest_transaction"]
  ) 
 
# TODO 72: Display: Largest Transaction
  col2.metric(
    "Largest Transaction",
    f"₱{result['largest_transaction']:,.2f}"
  )
 
# TODO 73: Display: Latest Activity
  col3.metric(
    "Latest Activity",
    result["latest_timestamp"]
  )

######### Learning Signature ######### 
#Programmed by: Chanelle Go
#Date Submitted: September 9, 2026
 
#Program Description: 
#This program creates GUI for viewing the transaction history. It displays the timestamp of the transaction, type, and amount.
#Reflection:
#I learned to create a table that creates a summary for what the other modules has done.
 
#AI Usage
#[/] No AI Assistance – Completed independently without AI.
#[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
#[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.