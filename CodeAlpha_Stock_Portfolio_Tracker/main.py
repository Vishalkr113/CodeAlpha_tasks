# Stock Portfolio Tracker

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

# Step 2: Portfolio dictionary
portfolio = {}

# Step 3: User input
n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    
    portfolio[stock] = quantity

# Step 4: Calculate total investment
total_investment = 0

print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock} -> {quantity} shares = ${value}")
    else:
        print(f"{stock} not found in price list!")

# Step 5: Display total
print(f"\nTotal Investment Value = ${total_investment}")

# Step 6: Save to file (optional)
with open("portfolio.txt", "w") as file:
    file.write("===== STOCK PORTFOLIO SUMMARY =====\n\n")
    
    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            value = stock_prices[stock] * quantity
            file.write(f"{stock} -> {quantity} shares = ${value}\n")
    
    file.write("\n-----------------------------------\n")
    file.write(f"Total Investment Value = ${total_investment}\n")