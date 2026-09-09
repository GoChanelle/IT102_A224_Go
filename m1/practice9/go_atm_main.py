import streamlit as st
 
# TODO 1: Import the Account class.
from go_atm_account import Account
 
 # TODO 2: Import the balance module.
import go_atm_balance
  
# TODO 3: Import the deposit module.
import go_atm_deposit
 
# TODO 4: Import the withdraw module.
import go_atm_withdraw
 
# TODO 5: Import the history module.
import go_atm_history
 
# TODO 6: Import the analysis module.
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
    "Enter withdrawal amount"
    min_value=0.0,
    step=100.0,
    format="%.2f"
  )
 
# TODO 31: Create the Withdraw Money button.
  if st.button("Withdraw Money"):
 
# TODO 32: Check whether the withdrawal amount is valid.
    if amount <= 0
 
 
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
        st.succes("Withdrawal successful.")
 
# TODO 38: Display the updated balance. 
        st.metric(
          "New Balance",
          f"P{account.check_balance():,.2f}"
        )

######### Learning Signature ######### 
#Programmed by: Chanelle Go
#Date Submitted: September 9, 2026
 
#Program Description: 
#This program creates GUI for withdrawing money. It imports the withdraw_money function and accepts an amount through a number input.
#Reflection:
#I learned that a button can check if an amount is valid and a number input is used to add money.
 
#AI Usage
#[/] No AI Assistance – Completed independently without AI.
#[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
#[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.