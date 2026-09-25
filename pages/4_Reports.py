import streamlit as st
import pandas as pd

from modules.reports import get_monthly_report
from modules.transactions import get_transactions


st.title("Financial Reports")
st.write("Generate a monthly summary of your financial activity.")


# -----------------------------
# Select Month and Year
# -----------------------------

st.header("Monthly Report")

col1, col2 = st.columns(2)

with col1:
    selected_month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=9
    )

with col2:
    selected_year = st.number_input(
        "Year",
        min_value=2024,
        max_value=2100,
        value=2026
    )


# -----------------------------
# Generate Report
# -----------------------------

if st.button("Generate Report"):

    report = get_monthly_report(
        selected_month,
        selected_year
    )

    if report:

        st.subheader(
            f"Report for {selected_month}/{selected_year}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Income",
                f"₹{report['income']:.2f}"
            )

        with col2:
            st.metric(
                "Total Expense",
                f"₹{report['expense']:.2f}"
            )

        with col3:
            st.metric(
                "Balance",
                f"₹{report['balance']:.2f}"
            )

        # -----------------------------
        # Report Status
        # -----------------------------

        if report["balance"] > 0:
            st.success("Income is higher than expenses for this month.")
        elif report["balance"] < 0:
            st.warning("Expenses are higher than income for this month.")
        else:
            st.info("Income and expenses are equal for this month.")

    else:
        st.info("No report data available.")


# -----------------------------
# All Transactions
# -----------------------------

st.divider()

st.header("Transaction Records")

transactions = get_transactions()

if transactions:

    df = pd.DataFrame(transactions)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No transaction records available.")