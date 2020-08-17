'''
Given words first and second, consider occurrences in some text of the 
form "first second third", where second comes immediately after first, and 
third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", 
second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
'''
def OccuranceAfterBigram(text, first, second):
    
    words = text.split(' ')
    output = []
    for idx, word in enumerate(words):
        if word == first:
            if (idx+1 < len(words)):
                if(words[idx+1] == second):
                    if (idx+2 <len(words)):
                        output.append(words[idx+2])
       
            
    return output


print(OccuranceAfterBigram("alice is a good girl she is a good student", 'a', 'good'))

