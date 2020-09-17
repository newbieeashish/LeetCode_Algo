'''
You are climbing a stair case. It takes n steps to reach to the 
top.

Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def ClimbingStairs(n):
    if n == 1:
        return 1
         
        # to step 1, we can reach in max 1 way
        # to step 2, we can reach in max 2 ways (directly 
        # go to step 2 or go to step 1, then go to step 2)
        
    cost_at_previous_previous = 1
    cost_at_previous = 2
        
    for i in range(3, n+1):
        current_cost_would_be = cost_at_previous + cost_at_previous_previous
        cost_at_previous_previous = cost_at_previous
        cost_at_previous = current_cost_would_be
    
    return cost_at_previous 

print(ClimbingStairs(3))
