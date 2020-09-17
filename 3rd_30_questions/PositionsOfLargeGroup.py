'''
In a string s of lowercase letters, these letters form consecutive 
groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups 
"a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and 
end denote the start and end indices (inclusive) of the group. 
In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing 
order by start index.

 

Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 
and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are 
large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
Example 4:

Input: s = "aba"
Output: []
'''


def largeGroupPosition(s):
    output = []
    i = 0

    while i < (len(s) -1):  #iteration for non repeating elements
        j = i

        while j<(len(s)-1) and s[j] == s[j+1]: #iteration for repeating elements
            j +=1
        
        if (j-i+1)>= 3 : #checking condition for length 3 or more
            output.append([i,j])
        
        i = j
        i+=1
    return output

print(largeGroupPosition('abcdddeeeeaabbbcd'))