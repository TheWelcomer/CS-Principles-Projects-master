#------------------------------------Stock Storage-----------------------------------------

money = [100000]
stocking = []
pricing = []
sharing = []
naming = []
costing = []

#----------------------------------Intros & Imports----------------------------------------


def intro():
  print('Welcome to the Stock Market Simulator! Here, you can invest in real stocks using virtual money to create a virutal portfolio. You can see how your investments would pan out in real life and learn investment strategies, all while not risking any actual money! You can:\n\n A. Buy/Sell Stocks\n\n B. Study a company\n\n C. View portfolio\n\n D. Learn about the stock market\n\nType "?" to see these options again\n\nNote: to pick an option, type out its cooresponding letter and press enter)')
def learning_intro():
  print("\n\n\nWelcome to the stock learning center! Here, you can recieve information about the stock market along with basic tips and strategies for investing. Here's some of the questions I can help answer:\n\n A. What is a stock?\n\n B. What is a stock investment, and why do people invest?\n\n C. Can you give me some tips about investing?\n\n D. How do I decide when and what to buy/sell?\n\n E. Could you define what some of these crazy words like ticker symbol and portfolio mean?\n\n F. Exit learning center, I'm ready to invest!\n\nNote: to pick an option, type out its cooresponding Upper Case letter and press enter\n\n")
def research_intro():
  print("\n\n\nWelcome to the stock research center! Here, you can recieve recent and long-term pricing information about any stock on the market. In addition, you'll recieve basic information about the company, such as its products and purpose. By viewing this funamental and technicaldata, you can be better informed about the stocks you wish to purchase and the companies behind them. Please type in any stock name or ticker symbol, it's okay if you mispell, it'll still show up (probably).")

intro()

import lxml
import wikipedia
import random
import pandas as pd
import numpy as np
import urllib
from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

#-------------------------------------Main Parser------------------------------------------

data_type = ['span', 'span', 'span', 'span', 'td', 'td', 'span', 'span', 'span', 'span', 'span']
stock_data = ['50', '51', '98', '103', '117', '121', '124', '129', '137', '142', '147']

def all_parser(ticker):
  while True:
    try:
      data = []
      query = ticker + "stock yahoo finance"
      query = urllib.parse.quote_plus(query)
      number_result = 1
      ua = UserAgent()
      google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
      response = requests.get(google_url, {"User-Agent": ua.random})
      soup = BeautifulSoup(response.text, "html.parser")
      result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
      results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result if "url" in str(i)]
      links= [i.group(1) for i in results if i != None]
      string = links[0]
      string = (string[32:len(string)-1])

      url = 'https://finance.yahoo.com/quote/' + string + '/'
      page = requests.get(url)
      soup = BeautifulSoup(page.text, 'lxml')
      data.append(soup.find('title').text)
      num = 0

      for i in stock_data:
        if str(soup.find(data_type[num], {'data-reactid': i})) == 'None':
          result = "Can't find"
        else:
          result = soup.find(data_type[num], {'data-reactid': i}).text
        data.append(result)
        num = num + 1

      return(data)

    except:
      print("\n\nSorry, something went wrong, returning to main menu...\n\n\n")
      intro()
      main()

#-----------------------------------Buy/Sell Stocks----------------------------------------

def exchange():
  print("\n\n\nWelcome to the exchange! Here, you can buy a specified amount of a stock, or sell all your stock in a company you currently own. You currently have $",round(money[0], 2), " to invest and can either:\n\n\n A. Buy stock\n\n B. Sell stock")

  bell = input("\n\nWhat would you like to do?: ")

  if bell == 'A' or bell == 'a':
    print("\n\nPlease type in any stock name or ticker symbol, it's okay if you mispell, it'll still show up (probably). Note: if you are buying more of a stock you already own, I suggest selling the currently owned position and buying back a larger position. Otherwise, they'll show up as two different investments in the same stock.")
    ticker = input("\n\nWhat stock would you like to buy?: ")
    data = all_parser(ticker)
    name = data[0]
    price = data[1]
    day_change = data[2]

    print('\n\nSo you want to buy', name[0:len(name)-51], 'at $', price, ' (up/down ', day_change, 'today)? You currently have $', money[0], )
    confirm = input('\nPress y to proceed or anything else to cancel and return to the main menu: ')

    if confirm == 'Y' or confirm == 'y':
      print('\n\nHow much money worth of shares would you like to purchase? Your money entry will be rounded down to purchase a whole number of shares.')
      cost = input('\nHow much money would you like to invest?: ')
      print('\n\nAre you sure you want to make this purchase?')
      final = input('\nIf so, input y, or enter in anything else to return to the main menu: ')

      if final == 'Y' or final == 'y':
        print('\n\nFulfilling order...')
        data = all_parser(ticker)
        price = data[1]
        price = price.replace(',','')
        print(cost)
        print(price)
        lengh = len(price)
        pricer = price[2:lengh-2]
        print(pricer)
        shares = float(cost)//float(pricer)
        shares = float(shares)
        price = float(pricer)

        if (shares * price) < money[0]:
          if shares == 0:
            print("\n\nSorry, the order wasn't fulfilled, probably because you didn't spend enough money to buy a full share in your stock. Remember, you specify how much money you want to spend, not how many shares you want to buy. It's okay, we'll send you to the main menu, but come back and try again!\n\n\n")
            intro()
            main()
            
          else:
            stocking.append(str(ticker))
            sharing.append(shares)
            pricing.append(price)
            naming.append(name)
            costing.append(shares * price)
            money[0] = money[0] - (shares * price)
            print('\n\nOrder successfully fulfilled! Check out your portfolio for an update on this stock. Returing to main menu...\n\n\n')
            time.sleep(3)
            intro()
            main()


        else:
          print("\n\nSorry, the order wasn't fulfilled, probably because you spent more money than you have (Note: the price of shares also changes by the second; you may have had enough money before, but the price increased and now you don't). It's okay, we'll send you to the main menu, but come back and try again!\n\n\n")
          intro()
          main()
    
    else:
      print('\n\nOk then, returning to main menu...\n\n\n')
      intro()
      main()
  

  if bell == 'B' or bell == 'b':

    num = 0
    print("\n\nBelow are all the stocks you own:\n")

    for i in stocking:
      data = all_parser(i)
      name = data[0]
      price = data[1]
      day_change = data[2]
      price = price.replace(',','')
      value = float(price) * sharing[num]
      print('\n', num + 1, '. ', name[0:len(name)-51], ',  Total Value of Position: $', value)
      num = num + 1

    print("\n\nEnter the cooresponding number of a stock above to sell it. Note: you can't sell part of a position, you have to sell the entire chosen position. If you want to sell only part of a position, sell it all and buy a smaller number of shares back.")
    sell_pos = input('\n\nWhich position do you want to sell?: ')

    if int_detect(sell_pos) == True and 1 <= int(sell_pos) <= (len(sharing)):
      sell_pos = int(sell_pos)
      sell_pos = sell_pos - 1
      data = all_parser(stocking[sell_pos])
      name = data[0]
      price = data[1]
      day_change = data[2]
      price = price.replace(',','')
      value = float(price) * sharing[sell_pos]

      print('\n\nSo you want to sell ', name[0:len(name)-51], ' at $', price, ' (up/down ', day_change, " today)? The position's total value is $", round(value, 2), ' and you currently have $', money[0])

      confirm = input('\n\nPress y to proceed or anything else to cancel and return to the main menu: ')

      if confirm == 'y' or confirm == 'Y':
        print('\n\nFulfilling order...')
        data = all_parser(stocking[sell_pos])
        price = data[1]
        price = price.replace(',','')
        value = float(price) * float(sharing[sell_pos])
        money[0] = money[0] + value
        del stocking[sell_pos]
        del pricing[sell_pos]
        del sharing[sell_pos]
        del naming[sell_pos]
        del costing[sell_pos]
        print('\n\nOrder successfully fulfilled! Returing to main menu...\n\n\n')
        time.sleep(3)
        intro()
        main()

      else:
        print('\n\nOk then, returning to main menu...\n\n\n')
        intro()
        main()

    else:
      print("Sorry, that's not an option! Returning to main menu...")
      intro()
      main()

  else:
    intro()
    main()

def int_detect(sell_pos):
  try:
    int(sell_pos)
    return True
  except ValueError:
    print("That's not an option, try typing only a number. Returning to main menu...")
    intro()
    main()


#-----------------------------------Company Research---------------------------------------

def research():
  research_intro()
  print('\n\nNote: type "exit" to return to the main menu')
  ticker = input('\n\nWhich company do you want to research?: ')

  if ticker == 'exit' or ticker == 'Exit':
    print('\n')
    intro()
    main()

  else:

    data = all_parser(ticker)
    name = data[0]
    price = data[1]
    day_change = data[2]
    prev_close = data[3]
    day_open = data[4]
    range_day = data[5]
    range_year = data[6]
    volume = data[7]
    reg_volume = data[8]
    market_cap = data[9]
    beta = data[10]
    eps = data[11]

    print('\n\nCompany: ', name[0:len(name)-51], ' -Yahoo Finance')
    print('\nCurrent Price: ', price)
    print('\nPrice Change Today: ', day_change)
    print('\nPrevious Close: ', prev_close)
    print("\nOpening Price: ", day_open)
    print('\nTrading Range Today: ', range_day)
    print('\n52 Week Price Range: ', range_year)
    print("\nToday's Trading Volume: ", volume)
    print('\nTypical Trading Volume: ', reg_volume)
    print('\nMarket Capitalization: ', market_cap)
    print('\nBeta (the higher, the more volatile): ', beta)
    print('\nEarnings Per Share: ', eps)
    print('\n\nSome fundamental data from wikipedia: ', wiki_search(name))
    research()

def wiki_search(name):
  while True:
    try:
      return(wikipedia.summary(name[0:len(name)-51],5))
    except:
      return('There was a mistake with the wikipedia search, sorry')

#--------------------------------------Portfolio-------------------------------------------

def portfolio():
  print("\n\n\nWelcome to your stock portfolio! Here, you can track the increase/decrease in price of all your stocks and see where your money is currently being invested. If no positions are listed in your portfolio, it means you havn't made a purchase yet.\n\n\n Cash: $",money[0], "\n\n\n")

  num = 0
  values = []
  summing = 0

  for i in stocking:
    data = all_parser(i)
    name = data[0]
    price = data[1]
    day_change = data[2]
    prev_close = data[3]
    day_open = data[4]
    range_day = data[5]
    range_year = data[6]
    volume = data[7]
    reg_volume = data[8]
    market_cap = data[9]
    beta = data[10]
    eps = data[11]

    print('\n\n\nInvestment', num + 1, ': ',name[0:len(name)-51])

    day_changey = day_change[len(day_change)-8:len(day_change)-1]
    day_changey = day_changey.replace('(','')
    day_changiest = day_changey
    day_changey = day_changey.replace('+','')
    day_changey = day_changey.replace('-','')
    print(day_changey)
    day_changey = float(day_changey.replace('%',''))
    day_profit = day_changey * sharing[num]
    neg = day_changiest.find('-')
    
    round(day_profit, 2)
    round(day_changey, 2)

    if neg == '-1':
      print("\nToday's Loss: -$", round(day_profit, 2), " (-", day_changey, "%)")

    else:
      print("\nToday's Profit: +$", round(day_profit, 2), " (+", day_changiest, "%)")

    pricey = price.replace(',','')
    profity = ((pricing[num] - float(pricey)) * sharing[num])
    profity = str(profity)
    negy = profity.find('-')
    profity = float(profity)
    percenty = profity / (pricing[num] * sharing[num])
    profity = round(profity, 2)
    percenty = round(percenty, 2)
    profity = str(profity)

    if negy == '-1':
      new = '-$' + profity[1:len(profity)]
      print ('\nTotal Loss: ', new, ' (', percenty, '%)')
    else:
      new = '+$' + profity
      print ('\nTotal Profit: ', new, ' (+', percenty, '%)')

    value = float(sharing[num]) * float(pricey)
    values.append(value)
    
    print('\nTotal value of shares: $', value)

    print('\nNumber of shares: ', round(sharing[num], 0))

    print('\nBuying Price: ', pricing[num])

    print('\nCurrent Price: ', price)

    

    print('\nPrice Change Today: ', day_change)
    print('\nPrevious Close: ', prev_close)
    print("\nOpening Price: ", day_open)
    print('\nTrading Range Today: ', range_day)
    print('\n52 Week Price Range: ', range_year)

    num = num + 1
  
  for i in values:
    summing = summing + i
  
  summing = summing + money[0]
  print('\n\n\nTotal value of all assets: $', round(summing, 2), '\n\n\n')

  intro()
  main()

#----------------------------------Learn About Stocks--------------------------------------

def learning():
  lesson = input('What would you like to learn? ')

  if lesson == 'A' or lesson == 'a':
    print("\nA stock is an investment that represents a share, or partial ownership, of a company. As the value of a company increases or decreases, so too does its coorestponding stock price. Stock in a company is traded at a stock market, where the price increases or decreases depending on the supply and demand of the stock (aka, if more people are buying a stock than selling it, the price will increase; if more people are selling than buying, then the stock's price will decrease)\n\n")
    learning()

  if lesson == 'B' or lesson == 'b':
    print("\nPeople invest in a stock in the hopes that its price will increase in the future, allowing them to eventually sell it for a profit. In general, most stocks and the stock market as a whole tends to go up overtime, so having money in a variety of stocks can be very profitable even if they companies they represent perform moderatley well. The main benefits of investing in stocks are high returns and its ease of investing. The average returns for the stock market is 10% a year (7% when adjusted for inflation), so you can expect a dollar you invest today to have the buying power of two dollars in 10 years. The downside is the high instability of stocks. Invidivual stocks could drop 50%+ in a couple years or even months. Even a well balanced account can experience huge losses in mere months, such as when the entire value of the stock market dropped by half in the great recession.\n\n")
    learning()

  if lesson == 'C' or lesson == 'c':
    print(" First off, no matter how smart or how much experience you have, you can't consistently predict which stocks will outperform the market. Even the most sophisticated hedge funds and investors can't pick stocks that consistently outperform the market.\n\n")
    learning()

  if lesson == 'D' or lesson == 'd':
    print("\nThere's two fields of thought when it comes to deciding when to buy and sell. In fundamental trading, you want to buy stocks that are valued much lower, or sell stocks that are valued much higher, than the business they represent (Ie. this company just released a revolutionary new battery, but its stock is still priced as if the breakthrough never happened). In technical trading, patterns in the stock price are searched for and taken advantage of (Ie. The stock price has swung between $20 and $50 for the past 2 years, so I should buy the stock at $20 and hope to sell it near $50).\n\n")
    learning()

  if lesson == 'E' or lesson == 'e':
    print("\n\n\n Buy: Means to take a position or to buy shares in a company.\n\n\n Sell: Getting rid of the shares that you purchased, either because you've achieved your goal or because you want to cut your losses.\n\n\n Bull Market: A market condition that means stock prices are expected to rise.\n\n\n Bear Market: A market in which investors expect stock prices to fall.\n\n\n Volatility: How fast a stock moves up and down.\n\n\n Liquidity: How easily you can get into and out of an investment.\n\n\n Trading Volume: The number of shares being traded each day.\n\n\n Going Long: Betting that a company's stock will increase in price so that you can buy low and sell high.\n\n\n Averaging Down: Buying more of a stock as the price goes down. This results in a decrease of the average price at which the stock was purchased.\n\n\n Market Capitalization: What the market thinks a company's value is.\n\n\n IPO: Abbreviation for Initial Price Offering. The act of a private company selling shares on the market to become public.\n\n\n Blue Chip Stocks: Large, industry-leading companies offering stable dividend payments.\n\n\n Hedge/Mutual Funds: Accounts you can put money into. This money is then invested accross hundreds of stocks.\n\n\n ETFs: Aka, Exchange Traded Funds. They're like stocks, because you can buy and sell shares, but they're also mutual funds, because their value is derived from a mix of hundreds of stocks.\n\n\n Broker: A person who buys or sells investment for you, in exchange for a fee.\n\n\n Day Trading: The practice of buying and selling within the same trading day, before the close of the markets on that day.\n\n\n Dividend: A portion of a company's earnings that is paid to shareholders, the people that own that company's stock, on a quarterly or annual basis.\n\n\n Exchange: A place in which different investments are traded. The most well known in the US are the New York Stock Exchange (NYSE) and NASDAQ.\n\n\n Portfolio: A collection of investments owned by an investor.\n\n\n Sector: A group of stocks that are in the same business, such as Apple and Microsoft both falling under the Technology sector.\n\n\n Ticker Symbol: A one to four character  string of alphabetic letters that represents a publically traded company on a stock exchange.\n\n\n")
    learning()

  if lesson == 'F' or lesson == 'f':
    print("\nThanks for stopping by! Returning to main menu...\n\n\n")
    intro()
    main()

  if lesson == '?':
    learning_intro()
    learning()

  else: 
    print("\nSorry, that is not part of my functionality! Taking you back to the main menu...\n\n\n")
    intro()
    main()

    
#-------------------------------------Main Runner------------------------------------------

def main():
  section = input("\n\nWhat would you like to do? ")

  if (section == "A") or (section == "a"):
    exchange()
    intro()
    main()

  if (section == "B") or (section == "b"):
    research_intro()
    research()

  if (section == "C") or (section == "c"):
    portfolio()

  if (section == "D") or (section == "d"):
    learning_intro()
    learning()

  if (section == "?"):
    intro()
    main()

  else:
    print("Sorry, that is not part of my functionality! Please refer to the list of my functions by typing a question mark! ")
    main()

main()


#---------------------------------------Sources--------------------------------------------

#The medium, for help implementing Beutiful Soup Code, https://medium.com/analytics-vidhya/how-to-get-stock-prices-in-real-time-using-python-2021-bf50c1d2378b
#Yahoo Finance, for all the info from the markets that I parse in.
#Predictive Hacks, for their super useful google search parse code, https://predictivehacks.com/how-to-scrape-google-results-for-free-using-python/
#All the modules that I'm using, they're all super helpful