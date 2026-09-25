import streamlit as st

from modules.categories import get_categories
from modules.transactions import (
    add_transaction,
    get_transactions,
    delete_transaction
)


st.title("Transactions")
st.write("Add and view your income and expense transactions.")

# -----------------------------
# Add Transaction
# -----------------------------

st.header("Add Transaction")

categories = get_categories()

if categories:

    category_names = [category["category_name"] for category in categories]

    with st.form("transaction_form"):

        transaction_type = st.selectbox(
            "Transaction Type",
            ["Income", "Expense"]
        )

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=50.0
        )

        category_name = st.selectbox(
            "Category",
            category_names
        )

        description = st.text_input(
            "Description"
        )

        transaction_date = st.date_input(
            "Date"
        )

        submitted = st.form_submit_button(
            "Add Transaction"
        )

        if submitted:

            if amount <= 0:

                st.error("Amount must be greater than zero.")

            elif not description.strip():

                st.error("Description cannot be empty.")

            else:

                category_id = next(
                    category["category_id"]
                    for category in categories
                    if category["category_name"] == category_name
                )

                success = add_transaction(
                    transaction_type,
                    amount,
                    category_id,
                    description,
                    transaction_date
                )

                if success:

                    st.success("Transaction added successfully!")

                    st.rerun()

                else:

                    st.error(
                        "Unable to save the transaction. "
                        "Please check the database connection."
                    )
else:
    st.warning("No categories available.")


# -----------------------------
# Transaction History
# -----------------------------

st.divider()

st.header("Transaction History")

transactions = get_transactions()

if transactions:

    st.dataframe(
        transactions,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No transactions found.")
    
# -----------------------------
# Delete Transaction
# -----------------------------

if transactions:

    st.divider()

    st.header("Delete Transaction")

    transaction_options = {
        f"ID {transaction['transaction_id']} | "
        f"{transaction['type']} | "
        f"₹{transaction['amount']} | "
        f"{transaction['description']}": transaction["transaction_id"]
        for transaction in transactions
    }

    selected_transaction = st.selectbox(
        "Select a transaction to delete",
        list(transaction_options.keys())
    )

    if st.button("Delete Selected Transaction"):

        transaction_id = transaction_options[selected_transaction]

        success = delete_transaction(transaction_id)

        if success:
            st.success("Transaction deleted successfully!")
            st.rerun()
        else:
            st.error("Unable to delete the transaction.")