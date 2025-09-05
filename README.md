🧮 Risk Profiling & Portfolio Recommendation System

This project is a Flask-based financial advisory tool that helps users assess their risk profile and generates personalized investment portfolio recommendations across different asset classes:

📈 Equity (Stocks)

📊 Mutual Funds

🏦 Multi-Asset Allocation (Equity + Bonds + Gold)

The system uses rule-based risk scoring and dynamic allocation strategies to recommend 7–8 diversified assets (or mutual funds) tailored to the user’s preferences, budget, and risk appetite.

🚀 Features

✅ Interactive risk profiling (age, salary, dependents, drawdown tolerance, etc.)
✅ Categorizes investors into Low Risk 🛡️, Medium Risk ⚖️, or High Risk 🚀 profiles
✅ Portfolio recommendations:

Equity → Stock selection with unit allocation & cost distribution

Mutual Funds → Diversified mix of large, mid, small, sectoral, and debt funds

Multi-Asset Allocation → Weighted mix of equity, bonds, and gold ETFs with real unit allocation
✅ Supports sector preference filtering
✅ Dynamic allocation ensuring at least 1 unit per selected stock/fund
✅ Flask REST API endpoints for programmatic access
✅ CLI (interactive input) mode for local testing


