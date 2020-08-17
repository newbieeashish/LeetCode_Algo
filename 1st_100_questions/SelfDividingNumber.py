'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, 
and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
 dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''

def SelfDividingNumber(left,right):
    output = []
    for i in range(left, right+1):
        number = 1
        flag = 0
        
        while i>0:
            last_digit = i%10

            if last_digit !=0:
                if number%last_digit !=0:
                    flag =1
                    break
            else:
                flag = 1
                break
        if flag ==0:
            output.append(number)
        
    return output

print(SelfDividingNumber(1,22))
