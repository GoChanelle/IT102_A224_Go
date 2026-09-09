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


######### Learning Signature ######### 
#Programmed by: Chanelle Go
#Date Submitted: September 9, 2026
 
#Program Description: 
#This program creates the main menu and sidebar for Python ATM.
#Reflection:
#I learned how to launch a streamlit page and connect my Github to Streamlit.
 
#AI Usage
#[/] No AI Assistance – Completed independently without AI.
#[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
#[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
   