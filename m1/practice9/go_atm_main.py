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
    "View History",
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