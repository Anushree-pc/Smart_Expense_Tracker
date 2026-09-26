# 💰 Smart Expense & Budget Tracker

> A Python-based personal finance management application that helps users track income and expenses, manage category-wise budgets, analyze spending patterns, and generate monthly financial reports.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.64.0-red?logo=streamlit)
![MySQL](https://img.shields.io/badge/MySQL-8.x-orange?logo=mysql)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Pytest](https://img.shields.io/badge/Tests-26%20Passed-success?logo=pytest)

---

## 📌 Overview

Managing personal finances can become difficult when income, expenses, budgets, and spending patterns are recorded manually or scattered across different places.

**Smart Expense & Budget Tracker** provides a centralized application for managing personal financial records.

The application allows users to:

- 💵 Record income and expenses
- 🏷️ Organize transactions using categories
- 🎯 Set category-wise monthly budgets
- 🚨 Receive budget usage alerts
- 📊 Analyze spending patterns
- 📈 View monthly spending trends
- 📄 Generate monthly financial reports
- 🗑️ Delete unwanted transactions

The project combines **Python, MySQL, and Streamlit** to provide a simple and interactive financial management system.

---

## 🎯 Problem Statement

Many individuals track their expenses using notebooks, spreadsheets, or scattered applications. These methods can make it difficult to understand where money is being spent and whether monthly spending is within budget.

The goal of this project is to develop a simple system that can:

1. Store financial transactions in a structured database.
2. Categorize income and expenses.
3. Allow users to create monthly budgets.
4. Analyze spending patterns.
5. Alert users when their budget usage becomes high.
6. Generate useful financial summaries and reports.

---

## ✨ Key Features

### 💸 Transaction Management

- Add income and expense transactions
- Select transaction categories
- Add descriptions and transaction dates
- View complete transaction history
- Delete existing transactions
- Input validation for transaction data

### 🎯 Budget Management

- Create category-wise monthly budgets
- Track actual spending against budgets
- Calculate remaining budget
- Monitor budget utilization
- Generate automatic budget alerts

### 🚨 Smart Budget Alerts

The system automatically checks budget utilization.

| Budget Usage | Alert |
|---|---|
| Below 80% | Normal |
| 80% – 99% | ⚠️ Warning |
| 100% or above | 🚨 Budget Exceeded |

This helps users identify categories where spending requires attention.

### 📊 Spending Analytics

The Analytics module provides:

- Total income
- Total expenses
- Current balance
- Category-wise spending
- Monthly expense trends
- Spending summaries

### 📄 Financial Reports

Users can generate monthly financial reports containing:

- Total income
- Total expenses
- Remaining balance
- Selected month and year

---

## 🧩 Major Modules

The application is organized into the following major modules:

| Module | Purpose |
|---|---|
| 💸 Transaction Management | Add, view and delete transactions |
| 🏷️ Category Management | Manage expense categories |
| 🎯 Budget Management | Create and monitor budgets |
| 📊 Analytics | Analyze spending and financial data |
| 📄 Reports | Generate monthly financial summaries |

---

## 🏗️ System Architecture


                 👤 User
                    │
                    ▼
          ┌───────────────────┐
          │     Streamlit     │
          │    Web Interface  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │   Python Modules  │
          │                   │
          │ • Transactions    │
          │ • Categories      │
          │ • Budgets         │
          │ • Analytics       │
          │ • Reports         │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │       MySQL       │
          │     Database      │
          └─────────┬─────────┘
                    │
                    ▼
          📊 Analytics & Reports