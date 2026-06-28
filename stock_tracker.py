
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

num = int(input("\nHow many different stocks do you own? "))

for i in range(num):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Result saved in portfolio.txt")