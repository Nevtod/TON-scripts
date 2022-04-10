import numpy as np # импорт бибилиотеки numpy
import matplotlib.pyplot as plt # импорт модуля matplotlib.pyplot
import math

weeksPerYear = 365 // 7
stakeYearPercent = 0.1
farmYearPercent = 0.43

#time in weeks
def get_profit(yearPercent, totalWeeks):
    """return a factor which shows how your money sum will increase after @totalWeeks 
    time with given annual percentage @yearPercent

    Args:
        yearPercent (float): annual percentage
        totalWeeks (int): how much time you are ready to wait :)

    Returns:
        float: profit factor which looks like (1 + profitPercent)
    """
    
    profitPeriod = 36 / 24 / 7  # as a part of a week
    curWeek = 0
    curTime = 0 # hours from start
    profit = 1
    while curWeek < totalWeeks:
        profit *= 1 + yearPercent * profitPeriod / weeksPerYear
        curTime += 36
        curWeek = curTime / 24 / 7   
    return profit
    
def plot(x, y, xlabel, ylabel, title):
    plt.figure(figsize=[8, 3])
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    plt.savefig("profit.png")
    
def plot2(xsPack, ysPack, xlabel, ylabel, title, legendsPack):
    plt.figure(figsize=[12, 8])
    plt.grid(True)
    for i in range(len(xsPack)):
        plt.plot(xsPack[i], ysPack[i], label= "" if legendsPack[i] == None else legendsPack[i])
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.legend()
    # plt.show()
    plt.savefig("profit.png")

weeks = 10 
alpha = np.linspace(0.75, 1.25, 1000)  #отношение нового курса к старому
currentTonExchangeRate = 1.7
futureTonExchageRate = alpha * currentTonExchangeRate

curDzeta = get_profit(stakeYearPercent, weeks) - 1 
curGamma = get_profit(farmYearPercent, weeks) - 1

S = 133 * 1.7 # dollars in start
S0 = S / 2 
incomeStake = 2 * S0 * alpha * (1 + curDzeta) - 2 * S0
incomeFarm = 2 * S0 * np.sqrt(alpha) * (1 + curGamma) - 2 * S0

plot2([futureTonExchageRate, futureTonExchageRate], [incomeStake, incomeFarm],
      f"Курс тона в долларах через {weeks} недель",
      f"Твой доход в долларах через {weeks} недель",
     f"Income $, если сначала было {S} баксов и курс тона сначала был {currentTonExchangeRate}",
      ["Если на стейке", "Если на фарме"])



