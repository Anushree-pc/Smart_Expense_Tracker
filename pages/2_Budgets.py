import streamlit as st

from modules.categories import get_categories
from modules.budgets import (
    add_budget,
    get_budget_status,
    check_budget_alerts
)


st.title("Budget Management")
st.write("Set category-wise budgets and monitor your spending.")


# -----------------------------
# Add Budget
# -----------------------------

st.header("Add Budget")

categories = get_categories()

if categories:

    category_names = [
        category["category_name"]
        for category in categories
    ]

    with st.form("budget_form"):

        category_name = st.selectbox(
            "Category",
            category_names
        )

        amount = st.number_input(
            "Budget Amount",
            min_value=0.0,
            step=100.0
        )

        month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=9
        )

        year = st.number_input(
            "Year",
            min_value=2024,
            max_value=2100,
            value=2026
        )

        submitted = st.form_submit_button(
            "Add Budget"
        )

        if submitted:
            if amount <= 0:
                st.error("Budget amount must be greater than zero.")
            elif month < 1 or month > 12:
                st.error("Month must be between 1 and 12.")
            elif year < 2000:
                st.error("Please enter a valid year.")
            else:
                category_id = next(
                    category["category_id"]
                    for category in categories
                    if category["category_name"] == category_name
                )
                success = add_budget(
                    category_id,
                    amount,
                    int(month),
                    int(year)
                )
                if success:
                    st.success("Budget added successfully!")
                    st.rerun()
                else:
                    st.error(
                        "Unable to save the budget. "
                        "Please check the database connection."
                    )
else:
    st.warning("No categories available.")


# -----------------------------
# Budget Status
# -----------------------------

st.divider()

st.header("Budget Status")

col1, col2 = st.columns(2)

with col1:
    selected_month = st.number_input(
        "Select Month",
        min_value=1,
        max_value=12,
        value=9
    )

with col2:
    selected_year = st.number_input(
        "Select Year",
        min_value=2024,
        max_value=2100,
        value=2026
    )


budget_status = get_budget_status(
    selected_month,
    selected_year
)

if budget_status:

    st.dataframe(
        budget_status,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No budgets found for the selected month.")


# -----------------------------
# Budget Alerts
# -----------------------------

st.divider()

st.header("Budget Alerts")

alerts = check_budget_alerts(
    selected_month,
    selected_year
)

if alerts:

    for alert in alerts:

        if "exceeded" in alert:
            st.error(alert)
        else:
            st.warning(alert)

else:
    st.success("No budget alerts. Your spending is within limits.")