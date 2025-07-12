import os

from flask import Flask, render_template, request

from asset_data import ASSET_DATA
from logic import (calculate_risk_score, categorize_risk_profile,
                   recommend_equity_portfolio, recommend_mf_portfolio,
                   recommend_multi_asset_portfolio_specific_funds)

# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form

        user_profile = {
            "drawdown": float(data['drawdown']),
            "salary": float(data['salary']),
            "dependents": int(data['dependents']),
            "age": int(data['age']),
            "investment_type": data['investment_type'],
            "sector_preference": None if data['sector_preference'].lower() == 'none' else data['sector_preference'],
            "total_investment_amount": float(data['total_investment_amount'])
        }

        risk_score = calculate_risk_score(user_profile)
        risk_profile = categorize_risk_profile(risk_score)

        if user_profile['investment_type'] == 'Equity':
            portfolio = recommend_equity_portfolio(
                risk_profile,
                user_profile["sector_preference"],
                user_profile["total_investment_amount"],
                ASSET_DATA
            )
        elif user_profile['investment_type'] == 'Mutual Funds':
            portfolio = recommend_mf_portfolio(
                risk_profile,
                user_profile["sector_preference"],
                ASSET_DATA
            )
        else:
            portfolio = recommend_multi_asset_portfolio_specific_funds(
                risk_profile,
                user_profile["total_investment_amount"],
                user_profile["sector_preference"],
                ASSET_DATA
            )

        return render_template("index.html", result=portfolio, profile=risk_profile, score=risk_score, user=user_profile)

    # ✅ Fix: Return something for GET requests
    return render_template("index.html", result=None, user={})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
