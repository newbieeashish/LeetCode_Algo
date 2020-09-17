'''
In a list of songs, the i-th song has a duration of time[i] 
seconds. 

Return the number of pairs of songs for which their total duration 
in seconds is divisible by 60.  Formally, we want the number of 
indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.


Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, 
which is divisible by 60.
'''

def numPairsDivisibleBy60(time):
    store = {}
    pair = 0
        
    for t in time:
        if 60-t%60 in store:
            pair += store[60-t%60]
                
        elif t%60 ==0 and 0 in store:
            pair += store[0]
                
        if t%60 not in store:
            store[t%60] = 0
        store[t%60] += 1

    return pair 

print(numPairsDivisibleBy60([60,60,60]))