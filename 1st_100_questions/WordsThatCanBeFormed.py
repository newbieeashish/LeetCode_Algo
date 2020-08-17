'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''
from collections import Counter
def WordsThatCanBeFormed(words, chars):
    ouput = 0
    chars = Counter(chars)
    for word in words:
        word_chars = Counter(word)
        if all(c in chars and word_chars[c] <= chars[c] for c in word_chars):
            ouput += len(word)
    
    return ouput

print(WordsThatCanBeFormed(["cat","bt","hat","tree"],"atach"))