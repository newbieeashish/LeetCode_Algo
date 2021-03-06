'''
Given an arbitrary ransom note string and another string containing letters 
from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

def RansomNote(ransomNote, magazine):
    for char in set(ransomNote):
        if magazine.count(char)<ransomNote.count(char):
            return False
    return True

print(RansomNote('aa','aab'))
