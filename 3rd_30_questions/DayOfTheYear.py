'''
Given a string date representing a Gregorian calendar date 
formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61

'''

def DayOfYear(date):
    dates = date.split('-')
    year, month, day = int(dates[0]), int(dates[1]), int(dates[2])
        
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    countDays = 0
    i = 0
		
    while i < month - 1:
        countDays += months[i]
        i += 1
			
    if i>=2 and year%4==0 and year>1900:
        countDays += 1
			
    countDays += day
    return countDays

print(DayOfYear('2019-01-09'))