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
n = int(raw_input())

nums = map(int, raw_input().split())	
print sorted(list(set(nums)))[-2]

#soln 
n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        tmp = largest
        largest = x
        secondlargest = tmp
    elif x > secondlargest and x != largest:
        secondlargest = x
print(secondlargest)

#soln 
print sorted(set(arr))[-2]

# soln 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr))[-2])


# Given the names and grades for each student in a class of  students, store them in a nested list and 
# print the name(s) of any 
# student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically 
# and print each name on a new line.

# The ordered list of scores is , so the second lowest score is . There are two students with that score: 
# . Ordered alphabetically, the names are printed as:


# sln

if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])


# if __name__ == '__main__':
    newlist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newlist.append([score, name])
        
    newlist.sort()
    list2 = [i for i in newlist if i[0] != newlist[0][0]]
    list3 = [x for x in list2 if x[0] == list2[0][0]]
    
    list3.sort(key=lambda j : j[1] )
    for i in range(len(list3)):
        print(list3[i][1])


#The provided code stub will read in a dictionary containing key/value pairs of
#  name:[marks] for a list of students. Print the average of the marks array for
#  the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))

#soln
marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print('%.2f' %(sum(marks[input()])/3))

#soln
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores=sum(scores)/3
        student_marks[name] = scores
    query_name = input()    
    print('%.2f' % student_marks[query_name])

#soln
n = int(raw_input())

### create empty dictionary
dict={}

### kick off 'for' loop for 'n' times as specified by first     user input

for line in range(n):

###  grabs next input for 'n' times (as defined above) -    info defined as the split elements in the input string (        split on space " ")

info = raw_input().split(" ")

### declares 'scores' as floats, which are defined as       everything from the first element '1' on - using the slice      ':'

scores = map(float, info[1:])

### set element 0 of info to the sum of the scores divided      by the float of the length of scores (e.g. 3 in this case)      which computes the average - this overwrites the score      inputs, leaving jus the name key  and average score (you    can see this by 'print dict')

dict[info[0]] = sum(scores) / float(len(scores))

### print float with 2 decimal places '.2f' is the relevent     string formatting. '%' is the placeholder for the variable

print "%.2f" % dict[raw_input()]


#soln
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    print("%.2f"%(sum(marks)/3))



#Given an integer, , and  space-separated integers as
#  input, create a tuple, , of those  integers. Then compute and print the result of .
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported

if __name__ == '__main__':
    n = int(raw_input())
    input_line = raw_input()
    input_list = input_line.split()
    for i in xrange(n):
        input_list[i] = int(input_list[i])
    t = tuple(input_list)
    print(hash(t))

#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    
    return s.swapcase()
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result 

#soln 2
def swap_case(s):
    result = ''
    for letter in s:
        if letter == letter.upper():
            letter += letter.lower()
        else:
            letter += letter.lower()
    return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird '''

if __name__ == '__main__':
    n = int(input().strip())
    
    if (n%2) == 1:
        print("Weird")
    elif (n%2) == 0 and n in range(2,5):
        print("Not Weird")
    elif (n%2) == 0 and n in range(6,20):
        print("Weird")
    elif (n%2) == 0 and n > 20:
        print("Not Weird") 



# split and join words 
a = "This is not a genuine code"
a  = a.split()
print(a)

a = " ".join(a)
print(a)


# smaple 2 on joining an spliting a string (we assume we getting inout from user)

def split_and_join(line):
    # write your code here
    line = line.split()
    line = "-".join(line)
    return line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# String formating, add first and last name to the given string 
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
    