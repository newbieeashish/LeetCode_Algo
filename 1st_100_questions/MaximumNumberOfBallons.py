'''
Given a string text, you want to use the characters of text to form as many 
instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of 
instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

Input: text = "leetcode"
Output: 0
'''

def MaximumNumberBallons(text):
    S = "balon"
    dir = dict()
        
    for s in S:
        if s in text:
            if s == 'l' or s == 'o':
                dir[s] = int(text.count(s)/2)
            else:
                dir[s] = text.count(s)
            text = text.replace(s, "")
        else:
            dir[s] = 0
        
    return min(dir.values())

print(MaximumNumberBallons("loonbalxballpoon"))
