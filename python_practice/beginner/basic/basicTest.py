# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


# works well but not all test pass because there is not else in the first loop

n = int(input())

if (n%2==0):
    if(n in range(2,5)):
        print("Not Weird")
    elif(n in range(6,20)):
        print("Weird")
    elif(n > 20):
        print("Not Weird")
else:
    print("Weird")


# OR [All the test pass here]

n = int(input())
if (n%2==0):
    if(n in range(2,6)):
        print("Not Weird")
    elif(n in range(6,21)):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")



# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers

a = int(raw_input())
b = int(raw_input())

print(a+b)
print(a-b)
print(a*b)


# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a//b)
print(a/b)


# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
# Example
# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

if __name__ == '__main__':
    n = int(raw_input())
    
    for i in range(n):
        print(i**2)
    
    
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar
#  for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

#sln 1
def is_leap(year):
    leap = False
    
    if(year%4==0) and (year%100!=0 or year%400==0):
        leap = True
    
    return leap

year = int(raw_input())


# sln 2
year=int(input("enter year to checjk"))

def check_year(year):
    leap = False
    if(year%100==0 or year % 400==0 or year%4==0):
        leap = True
    return leap
print(check_year(year))

# sln 3
def is_leap(year):
	return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

# sln 4
def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
	if (year % 400 == 0):
                leap = True
    return leap

#soln 5 
def is_leap(y):
    return (y%400==0) or (y%100!=0 and y%4==0)


# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.
# Example

# Print the string 12345

#sln 1
from __future__ import print_function
N = int(raw_input())
for i in range(1, N+1):
    print(i, end="")


#soln 
[print(i+1, end = '') for i in range(n)]

#soln 
[print(*range(1, int(input())+1), sep='')]


# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions 
# of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where 
# the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a 
# learning exercise.



#soln [not recomended because fo repetition ]
x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

# soln 2 [more precise]
x, y, z, n = int(input()) for _ in range((4)) # underscore is used because we wont be using the var
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

# oln 
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    print([[a,b,c]for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)
    if a + b + c != n])



# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.


# soln 




