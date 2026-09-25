import streamlit as st

from modules.analytics import get_financial_summary


st.title("Smart Expense Tracker")

st.write("Personal Finance Dashboard")


# =========================
# Financial Summary
# =========================

summary = get_financial_summary()

if summary:

    total_income = summary["total_income"]
    total_expense = summary["total_expense"]
    balance = summary["balance"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Income",
            f"₹{total_income}"
        )

    with col2:
        st.metric(
            "Total Expenses",
            f"₹{total_expense}"
        )

    with col3:
        st.metric(
            "Balance",
            f"₹{balance}"
        )

else:
    st.warning("Unable to load financial data.")


# =========================
# Welcome
# =========================

st.divider()

st.subheader("Welcome to Smart Expense Tracker")

st.write(
    "Use the sidebar to manage transactions, "
    "set budgets, analyze spending, and generate reports."
)