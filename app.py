import streamlit as st


st.set_page_config(
    page_title="Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)


dashboard = st.Page(
    "pages/Dashboard.py",
    title="Dashboard",
    icon="🏠"
)

transactions = st.Page(
    "pages/1_Transactions.py",
    title="Transactions",
    icon="💸"
)

budgets = st.Page(
    "pages/2_Budgets.py",
    title="Budgets",
    icon="💰"
)

analytics = st.Page(
    "pages/3_Analytics.py",
    title="Analytics",
    icon="📊"
)

reports = st.Page(
    "pages/4_Reports.py",
    title="Reports",
    icon="📄"
)


pg = st.navigation([
    dashboard,
    transactions,
    budgets,
    analytics,
    reports
])


pg.run()