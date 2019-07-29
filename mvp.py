import stocks

print("Welcome to the climate change and finance simulator game!")

print("Here is a list of the stocks available to invest in.")
list_unique_stocks = []

for stock in stocks.stocks_chart:
    if ((stock['symbol'] in list_unique_stocks) == False):
        list_unique_stocks.append(stock['symbol'])
print(list_unique_stocks)

balance = int(input("What is your current balance?\n"))
symbol = input("What is the symbol of the stock that you would like to buy?\n")
price = 0

year = input("During which of the years (1990, 2000, 2007) would you like to invest in this stock?\n")

for stock in stocks.stocks_chart:
    if (symbol == stock['symbol']) and (year == stock['year']):
        price = stock['price']

shares_all = balance // price
print("You are able to buy " + str(shares_all) + " shares of stocks " + symbol + " with your current balance.")
choice = int(input("What would you like to do? \n1. Buy all " + str(shares_all) + " shares\n2. Buy some shares\n3. Buy none\n" ))
sell_price = 0

if choice == 1:
    sell_year = input("At what year would you like to sell the stocks? (2000, 2007, 2019)\n")
    for stock in stocks.stocks_chart:
        if (sell_year == stock['year']) and (symbol == stock['symbol']):
            sell_price = stock['price']
    profit = (sell_price - price) * shares_all
    balance += profit
elif choice == 2:
    shares = int(input("How many shares would you like to buy?\n"))
    if shares < shares_all:
        sell_year = input("At what year would you like to sell the stocks? (2000, 2007, 2019)\n")
        for stock in stocks.stocks_chart:
            if (sell_year == stock['year']) and (symbol == stock['symbol']):
                sell_price = stock['price']
        profit = (sell_price - price) * shares
        balance += profit
    else:
        print("Please enter a valid number of shares under " + str(shares_all))
elif choice == 3:
    print("Thank you. Please come back and find out more about stocks int he future.")
    
print("You current balance is " + str(balance) + " dollars.")