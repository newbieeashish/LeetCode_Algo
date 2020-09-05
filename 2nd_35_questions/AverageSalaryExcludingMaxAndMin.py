'''
Given an array of unique integers salary where salary[i] is the salary of 
the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000
Example 3:

Input: salary = [6000,5000,4000,3000,2000,1000]
Output: 3500.00000
Example 4:

Input: salary = [8000,9000,2000,3000,6000,1000]
Output: 4750.00000
'''

def AvgSalary(salary):
    max_salary = max(salary)
    min_salary = min(salary)
    total = 0
    for i in salary:
        total +=i
    avg = (total-max_salary-min_salary)/(len(salary)-2)

    return avg

print(AvgSalary([6000,5000,4000,3000,2000,1000]))