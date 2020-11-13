import robin_stocks as r
import os 


login = r.login('email@gmail.com','password')


## Query AAPL 

positions_data = r.get_open_stock_positions()

prof = r.profiles.load_account_profile(info=None)

# print(prof)
inputSymbols = ["AAPL"]
aapl = r.stocks.get_fundamentals(inputSymbols, info=None)
print(aapl)

## Shit shit out 
file1 = open('symbols.txt', 'r') 
lines = file1.readlines() 

strip_lines = [] 

for line in lines: 
    strip_lines.append(line.strip())

print("Shitting out information for")
print(strip_lines)

market_caps = {} 
for symbol in strip_lines: 
    info = r.stocks.get_fundamentals(symbol, info=None)
    if info is not None: 
        if info[0] is not None: 
            cap = info[0]['market_cap']
            if cap is not None: 
                market_caps[symbol] = float(info[0]['market_cap'])
    # print(info)

print(market_caps)

## Sort market caps: 

sorted_market_caps = {k: v for k, v in sorted(market_caps.items(), key=lambda item: item[1])}
print(sorted_market_caps)