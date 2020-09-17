'''
Given two non-negative integers num1 and num2 represented as 
string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert 
the inputs to integer directly.
'''

def AddString(num1, num2):
    carry = 0
    number = ''
    if len(num1) > len(num2):
        num2 = '0' * (len(num1) - len(num2)) + num2
    elif len(num2) > len(num1):
        num1 = '0' * (len(num2) - len(num1)) + num1
    for a,b in map(lambda xy: (int(xy[0]), int(xy[1])), reversed(list(zip(num1, num2)))):
        carry, num = divmod(a+b+carry, 10)
        number=str(num)+number
    if carry == 1:
        number = '1'+number
    return number

print(AddString('12','12'))