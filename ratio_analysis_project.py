def calculate_roe(net_income, shareholders_equity):
    roe = net_income / shareholders_equity
    return roe

"""
Return on equity = net income / shareholder's equity. 
"""

def calculate_profit_margin(net_income, revenue):
    net_profit_margin = net_income / revenue
    return net_profit_margin

"""
profit margin = net income / revenue.
"""

def calculate_debt_to_equity(total_debt, shareholders_equity):
    debt_to_equity = total_debt / shareholders_equity
    return debt_to_equity

"""
debt to equity = total debt / shareholders
"""

def calculate_eps(net_income, shares_outstanding):
    eps = net_income / shares_outstanding
    return eps

"""
Earnings per share = net income / shares outstanding
"""

def calculate_pe_ratio(stock_price, eps):
    pe_ratio = stock_price / eps
    return pe_ratio

"""
Price to earnings ratio = stock price / earnings per share.
"""

def calculate_current_ratio(current_assets, current_liabilities):
    current_ratio = current_assets / current_liabilities
    return current_ratio

"""
Current ratio =  current assets / current liabilities
"""

def print_ratio_summary(company_name, roe, profit_margin, debt_to_equity, pe_ratio, current_ratio):
    print(f"===== Ratio Summary: {company_name} =====")
    print(f"ROE: {roe * 100:.2f}%")
    print(f"Profit Margin: {profit_margin * 100:.2f}%")
    print(f"Debt to equity ratio: {debt_to_equity:.2f}")
    print(f"PE ratio: {pe_ratio:.2f}")
    print(f"Current Ratio: {current_ratio:.2f}")

def main():

    companies = [
        {
            "name": "Meta Platforms",
            "net_income": 60458,
            "revenue": 201000,
            "shareholders_equity": 217243,
            "total_debt": 58744,
            "shares_outstanding": 2574,
            "stock_price": 669,
            "current_assets": 108722,
            "current_liabilities": 41836,
        },
        {
            "name": "Alphabet",
            "net_income": 132170,
            "revenue": 402836,
            "shareholders_equity": 415629,
            "total_debt": 46500,
            "shares_outstanding": 12090,
            "stock_price": 357,
            "current_assets": 206038,
            "current_liabilities": 102745,
        },
    ]

    results = []

    for company in companies:
        company_name = company["name"]
        net_income = company["net_income"]
        revenue = company["revenue"]
        shareholders_equity = company["shareholders_equity"]
        total_debt = company["total_debt"]
        shares_outstanding = company["shares_outstanding"]
        stock_price = company["stock_price"]
        current_assets = company["current_assets"]
        current_liabilities = company["current_liabilities"]

        roe = calculate_roe(net_income, shareholders_equity)
        profit_margin = calculate_profit_margin(net_income, revenue)
        debt_to_equity = calculate_debt_to_equity(total_debt, shareholders_equity)
        eps = calculate_eps(net_income, shares_outstanding)
        pe_ratio = calculate_pe_ratio(stock_price, eps)
        current_ratio = calculate_current_ratio(current_assets, current_liabilities)

        print_ratio_summary(company_name, roe, profit_margin, debt_to_equity, pe_ratio, current_ratio)

        results.append({
            "name": company_name,
            "roe": roe,
            "profit_margin": profit_margin,
            "debt_to_equity": debt_to_equity,
            "pe_ratio": pe_ratio,
            "current_ratio": current_ratio,
        })

    print("\n===== COMPARISON =====")
    for result in results:
        print(f"{result['name']}: ROE={result['roe']*100:.2f}%, "
              f"Profit Margin={result['profit_margin']*100:.2f}%, "
              f"P/E={result['pe_ratio']:.2f}")

    best_roe = max(results, key=lambda r: r["roe"])
    print(f"\nHighest ROE: {best_roe['name']} ({best_roe['roe']*100:.2f}%)")
    print("=======================\n")


     


if __name__ == "__main__":
     main()


"""
These numbers are real numbers from Metas's and Alphabet's FY2025 data.
The numbers are all in millions except stock price and EPS.
this section compares the two companies the user inputs and ultimately tells the user the company with the higher ROE
"""
