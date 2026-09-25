# Smart Expense & Budget Tracker

## 1. Project Overview

Smart Expense & Budget Tracker is a Python-based personal finance management application developed to help users record, manage, and analyze their income and expenses.

The application provides a simple web-based interface where users can manage transactions, create category-wise budgets, monitor spending, view financial analytics, and generate monthly reports.

The project uses Python for application logic, MySQL for data storage, and Streamlit for the user interface.

---

## 2. Problem Statement

Managing personal expenses manually can make it difficult to track spending patterns, maintain budgets, and understand overall financial performance.

The Smart Expense & Budget Tracker provides a centralized system for recording financial transactions, monitoring category-wise budgets, analyzing spending patterns, and generating useful financial reports.

---

## 3. Objectives

- Record income and expense transactions.
- Organize transactions using categories.
- Create monthly budgets for different categories.
- Monitor budget usage and remaining amounts.
- Generate budget alerts when spending approaches or exceeds the budget.
- Analyze spending patterns.
- Display financial summaries and spending trends.
- Generate monthly financial reports.
- Store financial data securely in a MySQL database.

---

## 4. Main Features

### Transaction Management
- Add income and expense transactions.
- Select transaction categories.
- Store transaction descriptions and dates.
- View transaction history.
- Delete unwanted transactions.
- Validate transaction inputs.

### Category Management
- Store expense and income categories.
- Retrieve available categories from the database.
- Add new categories when required.

### Budget Management
- Create category-wise monthly budgets.
- View budget status.
- Calculate spent and remaining amounts.
- Generate alerts when 80% or more of a budget is used.
- Display an exceeded-budget alert when spending reaches or exceeds 100%.

### Analytics
- Calculate total income.
- Calculate total expenses.
- Calculate current balance.
- Analyze category-wise spending.
- Display monthly expense trends.

### Reports
- Generate monthly financial reports.
- Display monthly income.
- Display monthly expenses.
- Calculate monthly balance.
- Display transactions for the selected period.

---

## 5. Technologies Used

- Python
- Streamlit
- MySQL
- MySQL Connector/Python
- Pandas
- Python-dotenv
- Pytest

---

## 6. Project Structure

```text
Smart_Expense_Tracker/
│
├── app.py
│
├── pages/
│   ├── Dashboard.py
│   ├── 1_Transactions.py
│   ├── 2_Budgets.py
│   ├── 3_Analytics.py
│   └── 4_Reports.py
│
├── modules/
│   ├── transactions.py
│   ├── categories.py
│   ├── budgets.py
│   ├── analytics.py
│   └── reports.py
│
├── database/
│   ├── connection.py
│   └── schema.sql
│
├── tests/
│   └── test_tracker.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── statement.md