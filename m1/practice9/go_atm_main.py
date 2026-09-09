import streamlit as st

from go_atm_account import Account
import go_atm_balance
import go_atm_deposit
import go_atm_withdraw
import go_atm_history
import go_atm_analysis


# ==========================================
# ATM ACCOUNT
# ==========================================

account = Account(
    "Juan Dela Cruz",
    10000.00
)


# ==========================================
# STREAMLIT PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Python ATM",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# ATM HEADER
# ==========================================

st.title("PYTHON ATM")

st.write(
    f"Welcome, **{account.account_name}**!"
)

st.divider()


# ==========================================
# SIDEBAR MENU
# ==========================================

st.sidebar.title("ATM MENU")

choice = st.sidebar.radio(
    "Select an option:",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)


# ==========================================
# 1. CHECK BALANCE
# ==========================================

if choice == "Check Balance":

    st.header("Check Balance")

    balance = (
        go_atm_balance.check_balance(account)
    )

    st.metric(
        "Current Balance",
        f"₱{balance:,.2f}"
    )


# ==========================================
# 2. DEPOSIT
# ==========================================

elif choice == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Deposit Money"):

        if amount <= 0:

            st.error(
                "Invalid deposit amount."
            )

        else:

            success = (
                go_atm_deposit.deposit_money(
                    account,
                    amount
                )
            )

            if success:

                st.success(
                    "Deposit successful."
                )

                st.metric(
                    "New Balance",
                    f"₱{account.check_balance():,.2f}"
                )