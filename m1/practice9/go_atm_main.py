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
st.write(f"Welcome, **{account.account_name}**!")
 
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
    "View",
    "Analyze Transactions",
  ]
)

# TODO 14: Check whether the selected option "Check Balance".
if choice == "Check Balance":
 
# TODO 15: Display a page header.
  st.header("Check Balance");
 
# TODO 16: Call the balance module and obtain the current account balance.
  balance = (go_atm_balance.check_balance(account))
 
# TODO 17: Display the balance using a Streamlit metric.
  st.metric(
    "Current Balance",
    f"P{balance:,.2f}"
    )