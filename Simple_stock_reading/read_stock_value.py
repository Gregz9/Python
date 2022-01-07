from matplotlib import pyplot
from statistics import mean 


def read_file(file_name): 

    stock_history = []

    stock_values = open(file_name)
    for price in stock_values: 
       # price_float = float(price.strip())
        stock_history.append(float(price.strip()))
   
    return stock_history

"""For this simple algorithm to perform better, a third parameter is added, which is called 'day'.
In contrast to parameter 'days', which gives the amount of days we would like to look back, the day
gives us a day we want to start at."""

def average_last_n_days(prices, days, day, arg = 'n'): 
    """This manually defined function returns teh average of stock prices for the last n days.
    Given that we cannot calculate values of the past given that n can be larger than a given index,
    we need to account for a possibilty where i < n."""

    if(days > day): 
        interval = prices[(-len(prices))+day: -len(prices)-1: -1]
      
    else: 
        interval = prices[(-len(prices))+day: ((-len(prices)-1)+day)-days: -1]
     
    if(arg == 'n'):
        return interval
    elif(arg == 'r'): 
        return interval[::-1]

    
        
def average_each_nth_day(prices, days):
    avg_last_10_days = []
    for i in range(-1, (-len(prices)-1), -1): 
        if(-len(prices)+days > i): 
            average = mean(prices[-len(prices)+days: -len(prices)-1: -1])
            avg_last_10_days.insert(0, average)
        else: 
            average = mean(prices[i: i-days-1: -1])
            avg_last_10_days.insert(0, average)
    return avg_last_10_days
   
def sell_n_buy(prices, average_prices) :

    bought = False 
    sold = False
    bought_for = []
    sold_for = []
    gain = []

    for i in range(1, len(prices)): 
        if((prices[i-1] < average_prices[i]) and (prices[i] >= average_prices[i]) and not bought): 
            bought = True
            sold = False
            bought_for.append(prices[i])
        elif((prices[i-1] >= average_prices[i]) and (prices[i] < average_prices[i]) and not sold):
            bought = False 
            sold = True
            sold_for.append(prices[i])
    
    for i in range(0, len(bought_for)): 
        print(f' Bought for: {bought_for[i]} \nSold for: {sold_for[i]} \nGain: {sold_for[i]-bought_for[i]}')
        gain.append(sold_for[i]-bought_for[i])
    print(f'Total gain of investement: {sum(gain)}')
    return

prices = read_file('apple.txt')
average = average_each_nth_day(prices,10)
sell_n_buy(prices, average)
#pyplot.plot(prices[800:len(prices)])
#pyplot.plot(average[800:len(average)])
#pyplot.show()
