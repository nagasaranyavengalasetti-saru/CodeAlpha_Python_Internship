stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

print("===== STOCK PORTFOLIO TRACKER =====")

portfolio = {}
total_investment = 0

while True:

    stock = input("\nEnter stock name or type 'done': ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity

    portfolio[stock] = {
        "quantity": quantity,
        "price": stock_prices[stock],
        "investment": investment
    }

    total_investment += investment

print("\n===== YOUR PORTFOLIO =====")

for stock, details in portfolio.items():

    print("\nStock:", stock)
    print("Quantity:", details["quantity"])
    print("Price:", details["price"])
    print("Investment:", details["investment"])

print("\nTotal Investment =", total_investment)