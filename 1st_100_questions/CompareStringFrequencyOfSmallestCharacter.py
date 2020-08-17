'''
Let's define a function f(s) over a non-empty string s, which calculates the 
frequency of the smallest character in s. For example, if s = "dcce" then 
f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer,
 where each answer[i] is the number of words such that f(queries[i]) < f(W), 
where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3
so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second 
query both f("aaa") and f("aaaa") are both > f("cc").
'''
def CompareStringFreqOfSmallestCharacter(queries, words):
    query_freqs = [s.count(min(s)) for s in queries]
    word_freqs = [s.count(min(s)) for s in words]
        
    result = [0] * len(query_freqs)
    for i,q in enumerate(query_freqs):
        for w in word_freqs:
            if q < w:
                result[i] += 1
        
    return result

print(CompareStringFreqOfSmallestCharacter(["bbb","cc"],["a","aa","aaa","aaaa"]))