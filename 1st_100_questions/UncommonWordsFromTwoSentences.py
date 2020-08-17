'''
We are given two sentences A and B.  (A sentence is a string of space separated 
words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and 
does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
'''

def UncommonWords(A, B):
    word_A = A.split()
    word_B = B.split()

    freq = {}
    output = []

    for word in word_A:
        freq[word] = freq.get(word,0)+1
    
    for word in word_B:
        freq[word] = freq.get(word,0)+1
    
    for word in freq:
        if freq[word] == 1:
            output.append(word)
    
    return output

print(UncommonWords("this apple is sweet",'this apple is sour'))