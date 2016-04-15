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
    print "Number of $25 coins: "+ str(coin25)
    print "Number of $10 coins: "+ str(coin10)
    print "Number of $5 coins: "+ str(coin5)
    print "Number of $1 coins: "+ str(coin1)
	totalCoins = len(table[-1])
    return totalCoins #return total coins required for the change

coins = [25,10,5,1] # denomination set
print dynamic(63,coins) #calling the function
