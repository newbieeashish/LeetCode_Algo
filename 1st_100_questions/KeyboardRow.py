'''
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard'''

'''
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]'''

def keyboardRow(words):
    line_1 = set("qwertyuiop")
    line_2 = set("asdfghjkl")
    line_3 = set("zxcvbnm")
    
    ans = []
    for word in words:
        word_set = set(word.lower())
        
        if word_set <=line_1 or word_set<=line_2 or word_set <= line_3:
            ans.append(word)
            
            
    return ans

print(keyboardRow(["Hello", "Alaska", "Dad", "Peace"]))
