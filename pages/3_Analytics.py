import streamlit as st
import pandas as pd

from modules.analytics import (
    get_financial_summary,
    get_category_expenses,
    get_monthly_expenses
)


st.title("Spending Analytics")
st.write("Analyze your income, expenses, and spending patterns.")


# -----------------------------
# Financial Summary
# -----------------------------

st.header("Financial Summary")

summary = get_financial_summary()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Income",
        f"₹{summary['total_income']:.2f}"
    )

with col2:
    st.metric(
        "Total Expense",
        f"₹{summary['total_expense']:.2f}"
    )

with col3:
    st.metric(
        "Balance",
        f"₹{summary['balance']:.2f}"
    )


# -----------------------------
# Category-wise Expenses
# -----------------------------

st.divider()

st.header("Category-wise Spending")

category_expenses = get_category_expenses()

chart_data = []

for row in category_expenses:

    if float(row["total_spent"]) > 0:

        chart_data.append({
            "Category": row["category_name"],
            "Amount": float(row["total_spent"])
        })


if chart_data:

    df = pd.DataFrame(chart_data)

    # Top spending category
    top_category = df.loc[
        df["Amount"].idxmax()
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Highest Spending Category",
            top_category["Category"]
        )

    with col2:
        st.metric(
            "Amount Spent",
            f"₹{top_category['Amount']:.2f}"
        )

    # Bar chart
    st.subheader("Spending by Category")

    st.bar_chart(
        df.set_index("Category"),
        y="Amount"
    )

    # Detailed table
    st.subheader("Category Spending Details")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No expense data available yet.")


# -----------------------------
# Monthly Spending Trend
# -----------------------------

st.divider()

st.header("Monthly Spending Trend")

monthly_expenses = get_monthly_expenses()

if monthly_expenses:

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    trend_data = []

    for row in monthly_expenses:

        trend_data.append({
            "Month": f"{month_names[row['month']]} {row['year']}",
            "Expenses": float(row["total_expense"])
        })

    trend_df = pd.DataFrame(trend_data)

    st.line_chart(
        trend_df.set_index("Month"),
        y="Expenses"
    )

    st.subheader("Monthly Expense Details")

    st.dataframe(
        trend_df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No monthly expense data available yet.")