# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170
}

total = 0

print(" Stock Portfolio Tracker ")

while True:
    stock = input("\nEnter Stock Name (AAPL/TSLA/GOOGLE/AMZN): ").upper()

    if stock not in stocks:
        print("Stock not found!")
        continue

    quantity = int(input("Enter Quantity: "))

    value = stocks[stock] * quantity
    total += value

    print(f"Value of {stock}: ${value}")

    choice = input("Add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\nTotal Investment Value: $", total)

# Save result in a text file
file = open("portfolio.txt", "w")
file.write("Total Investment Value: $" + str(total))
file.close()

print("Portfolio saved successfully in portfolio.txt")
