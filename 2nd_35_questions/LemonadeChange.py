'''
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time 
(in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
'''

def LemonadeChange(bills):
    if not bills:
        return True
    idx , n = 1 , len(bills)
    if bills[idx - 1] != 5:
        return False
    five_count = 1
    ten_count = 0
    while idx < n:
        if bills[idx] == 5:
            five_count += 1
        elif bills[idx] == 10:
            if five_count >= 1:
                five_count -= 1
                ten_count += 1
            else:
                return False
        elif bills[idx] == 20:
            if ten_count >= 1:
                if five_count >= 1:
                    five_count -= 1
                    ten_count -= 1
                else:
                    return False
            elif five_count >= 3:
                five_count -= 3
            else:
                return False
        idx += 1
    return True

print(LemonadeChange([10,10]))