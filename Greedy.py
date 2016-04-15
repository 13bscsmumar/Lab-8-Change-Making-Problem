import math
def greedy(money,coins):
    coinsUsed = [] # list for saving the coins used for change making
    totalCoins = 0
    coin25 = int(math.floor(money / coins[0])) # calculating the number of $25 coins for the given amount
    coinsUsed.append(coin25) # append the number to the list
    money = money -  coin25 * coins[0] # subtract the total that coins make, from the total money
    # similarly for other coins
    coin10 = int(math.floor(money/coins[1]))
    coinsUsed.append(coin10)
    money = money -  coin10 * coins[1]
    
    coin5 = int(math.floor(money/coins[2]))
    coinsUsed.append(coin5)
    money = money -  coin5 * coins[2]
    
    coin1 = int(math.floor(money/coins[3]))
    coinsUsed.append(coin1)
	
    for k in range(len(coinsUsed)): # calculating how many number of each coin is used for the change making
        if (coinsUsed[k] != 0):
            totalCoins +=coinsUsed[k] 
    print "##########Greedy#########" # printing details
    print "Total Number of coins: " + str(totalCoins)
    print "Number of $25 coins: "+ str(coinsUsed[0])
    print "Number of $10 coins: "+ str(coinsUsed[1])
    print "Number of $5 coins: "+ str(coinsUsed[2])
    print "Number of $1 coins: "+ str(coinsUsed[3])
    
    return totalCoins #returning totalCoins
	
	
coins = [25,10,5,1] # set/list of denominations
totalCoins = greedy(63,coins) # calling fucntion
print totalCoins # printing results
