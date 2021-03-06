'''
There are 2N people a company is planning to interview. The cost of flying 
the i-th person to city A is costs[i][0], and the cost of flying the i-th person 
to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N 
people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people 
interviewing in each city.
'''
def TwoCityScheduling(costs):
    n = len(costs)//2
        # calculate the difference between city A and city B for each person
    delta = [(a - b) for a, b in costs]
        # get the ordered difference
    ordered_delta = sorted((value, i) for (i, value) in enumerate(delta))
    minimum_cost = 0
        # for the n smallest cost_A - cost_B, it costs a lot to fly to B,
        # so we send them to city A
    for value, i in ordered_delta[:n]:
        minimum_cost += costs[i][0]
        # for the n greatest cost_A - cost_B, it costs a lot to fly to A,
        # so we send them to city B
    for value, i in ordered_delta[n:]:
        minimum_cost += costs[i][1]
    return minimum_cost

print(TwoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))