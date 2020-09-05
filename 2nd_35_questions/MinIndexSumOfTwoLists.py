'''
Suppose Andy and Doris want to choose a restaurant for dinner, and 
they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list 
index sum. If there is a choice tie between answers, output all of them 
with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is 
"Shogun" with index sum 1 (0+1).
'''

from collections import defaultdict
def MinIndexSumofTwoLists(list1,list2):
    
    d = defaultdict(int)
    for X,Y in [[list1,set(list2)],[list2,set(list1)]]:
        for i,a in enumerate(X):
            if a in Y:
                d[a] += i
    m = min(d.values())
    return [ k for k,v in d.items() if v==m ]
    
        



print(MinIndexSumofTwoLists(["Shogun", "Tapioca Express", "Burger King", "KFC"],
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))


    