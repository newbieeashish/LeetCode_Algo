'''
Given numBottles full water bottles, you can exchange numExchange empty 
water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty 
bottle.

Return the maximum number of water bottles you can drink.

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
Example 3:

Input: numBottles = 5, numExchange = 5
Output: 6
Example 4:

Input: numBottles = 2, numExchange = 3
Output: 2

'''

def WaterBottles(numBottles, numExchange):
    ouput = numBottles
    while numBottles>=numExchange:
        ouput += numBottles//numExchange
        numBottles = numBottles//numExchange + numBottles%numExchange
    
    return ouput

print(WaterBottles(15,4))
