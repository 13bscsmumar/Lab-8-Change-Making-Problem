import math
import math
def dynamic(money,coins):
    table=[] # table list for maintaining the results for reusing 
    newValue = money + 1
    for x in range(newValue):
        table.append(0) # appends 0 to table list
    table[0] = [] # creates list at 0th index of table
    for i in range(1, newValue):
        for j in coins:
            if j > i: continue # skip if coin value is greater than the amount of money 
            elif not table[i] or len(table[i - j]) + 1 < len(table[i]):
                if table[i - j] != None:
                    table[i] = table[i - j][:] #calulate and store the result 
                    table[i].append(j) #insert the coin value in the table 
    coin25 = 0
    coin10 = 0
    coin5 = 0
    coin1 = 0

    for i in range(len(table[-1])): # calculating number of each coins used
        temp = table[-1]
        if (temp[i] == 25):
            coin25+=1
        elif(temp[i] == 10):
            coin10+=1
        elif(temp[i] == 5):
            coin5+=1
        elif(temp[i] == 1):
            coin1+=1
    print "##########Dynamic#########" # printing details
    print "Total Number of coins: " + str(len(table[-1]))
    #print "Number of $25 coins: "+ str(coin25)
    #print "Number of $10 coins: "+ str(coin10)
    #print "Number of $5 coins: "+ str(coin5)
    #print "Number of $1 coins: "+ str(coin1)
	totalCoins = len(table[-1])
    return totalCoins #return total coins required for the change
	
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
    #print "Number of $25 coins: "+ str(coinsUsed[0])
    #print "Number of $10 coins: "+ str(coinsUsed[1])
    #print "Number of $5 coins: "+ str(coinsUsed[2])
    #print "Number of $1 coins: "+ str(coinsUsed[3])
    
    return totalCoins #returning totalCoins

import random
coins = [25,10,5,1] #set of denominations
for i in range (100): # trying with 100 random number in range 1-1000
    money = int(random.randint(1,1000)) # generates a random number between 1 - 1000
    gred = greedy(money,coins) # calls greedy function
    dynam = dynamic(money,coins) # calls dynamic function
    if (dynam<gred): # comparing total coins returned by each function
        print money # if dynamic approach is optimal coins would be less, hence print that amount of money
    else:
        print "not found for money value: " + str (money) #else print money not found for which dynamic is more optimal

