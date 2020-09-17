'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD 
as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
'''
from datetime import datetime
def NumberOfDays(date1, date2):
    start = datetime.strptime(date1, '%Y-%m-%d').date()
    end = datetime.strptime(date2, '%Y-%m-%d').date()
    return abs((end-start).days)

print(NumberOfDays('2019-06-29','2019-06-30'))
