'''
Given a positive integer num, output its complement number. The complement 
strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), 
and its complement is 0. So you need to output 0.'''

def NumberCompliment(num):
    return int(''.join('1' if b == '0' else '0' for b in bin(num)[2:]), 2)

print(NumberCompliment(5))