from __future__ import print_function
from __future__ import division
from curses import init_pair
from ntpath import join
from turtle import st
import requests
from bs4 import BeautifulSoup
import string
import random
import sys



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
year=int(input("enter year to check"))

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
	if(year % 400 == 0):
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


'''
Task Given an integer, , perform the following conditional actions:

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
       
# create a list and print only number less than 5 or equal to  in a list
# Example in a list of [2,3,4,5,11,1,16,7,8,9] -> [2,3,4,1]
nums = [1,2,4,3,2,5,7,9,44]
x = []
for i in nums:
    if i <= 5:
        x.append(i)
        x.sort()
print(x)  # returns a list of number less than 5 in a list given
print([j for j in nums if j<5]) # using one line solution to print the list



# User Input and Numerics
# get a user name, age and print to the the year they turn 100 years;

def year_100():
    name = input("Enter your name: ")
    age = int(input("What's your age: "))
    turn_100 = ((2022) + (100 - age))
    print(f" Hello {name} You will turn 100 years in the year {turn_100}")
    
year_100()


# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.
def check_divisibility():
    num = int(input("Enter num to check divisibility: "))
    check = int(input("Enter check number to divide: "))
    
    if(num % check == 0 and num % 4 == 0):
        print("This is a multiple of 4")
        ("This is an Even Number")
    elif (num % 2 == 0):
        print("Even Number")
    else:
        print("This is an odd number")
        
check_divisibility()



# print divisibility of a number in a given range. [use list,conditions and user input]
def get_divisor():
    num = int(input("Enter number to check divisibility: "))
    divisor_list = []
    list_range = list(range(1, num + 1))
    for number in list_range:
        if num % number == 0:
            divisor_list.append(number)
    print(divisor_list)            

get_divisor()            


def check_divisibility():
    user_number = int(input("Enter number to check divisibility"))
    list_range = list(range(1, user_number + 1))
    divisor_list = []
    for number in list_range:
        if(user_number % number == 0):
            divisor_list.append(number)
    print(divisor_list)
    
check_divisibility()    



# print only commin elements between 2 lists without duplicates

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(a) & set(b)))

# list comprehension
a = [1,2,3,4,5,6,8,9,4,3,5]
b = [1,6,9,33,22,6,788,3]
print([i for i in a if i in b])

#


# write  a program to check if a string is palidrome(Checks if read same as reverse oder)
def checkPalidrone():
    user_string = input("Enter string to check: ")
    if str(user_string) == str((user_string)[::-1]):
        print("Pallidrone")
    else:
        print("Not Pallidrone")

# print only even number in a list using list comprehension 
list_a = [2,3,5,7,9,12,38,90]
list_even = [x for x in list_a if x % 2 == 0]
print(list_even)


# Guess Game with while and if conditions;

def rock_scissor_paper():
    user_input = input("Enter a guess!: ")
    while user_input != "quit":
        if(user_input == "Rock"):
            print("Rock won....")
            break
        elif (user_input == "Scissors"):
            print("Scissors Won..")
            break
        elif(user_input == "Paper"):
            print("Paper won....")
            break
        else:
            user_input = input("Try another Guess. ")
    print("Game Ended...")
rock_scissor_paper()



# Rock paper and scissor Game:

user_name1 = input("Hello, What your name? ")
user_name2 = input("And you? ")
user_1 = input(f"Hey {user_name1}, Do you want to choose rock, scissor or paper?...")
user_2 = input(f"what about you {user_name2}, what do you choose?...")

def compare_game(u1, u2):
    if u1 == u2:
        return " Its a tie for you two"
    elif(u1 == "rock"):
        if (u2 == "scissor"):
            return "Rock wins !!"
        else:
            return "Paper wins !!"
    elif (u1 == "scissor"):
        if(u2 == "paper"):
            return "Scissor wins !!"
        else:
            return "Rock wins !!"
    elif (u1 == "paper"):
        if(u2== "rock"):
            return "Paper wins !!"
        else:
            return "Scissor wins !!"
    else:
        return "Try again, you did not select either Rock, Scissor or Paper"
        sys.exit()

print(compare_game(user_1,user_2))



# Random guess game:
def guess_game():
    guess = input("Enter a random number between 1 and 9")
    quit_game = "quit"
    guess_count = 0
    guess_number = 7
    while guess != guess_number and guess != "exit":   
                     
        if(guess == "exit"):
            break
        guess = int(guess)
        guess_count += 1
        
        if (guess < guess_number):
            print("Your guess too low..")
        elif(guess >guess_number):
            print("Guess too high")
        else:
            print(f"you guessed it right , its {guess_number} with {guess_count} trials only" )
                
guess_game()
    
    
# check if a number is prime or not

def check_prime():
    user_number = int(input("\n Enter number to check divisibility: "))
    if user_number > 1:
        for i in range(2,user_number//2):
            if(user_number%i  == 0):
                print("This is NOT Prime number")
                break
            else:
                print("This is a prime number")                
        
check_prime()


# write a program that takes in first and last elements in a list

def list_comprehension():
    
    a = [2,4,6,8,10]
    b = []
    b.append(a[0])
    b.append(a[-1])

    print(b)
# Or
list_comprehension()

def list_comp(list_a):
    return [list_a[0], list_a[len(list_a) - 1]]
    
print(list_comp([2,3,4,4,5,6]))


## write a funtion that will retrun a list not containing duplicates.

list_a = ["timz","owen","timo","TimTim","Timz","owen","timz","Timo"]
list_b = ["owen","timz","timtim","owen","andela"]
new_list = []

def remove_duplicates(): # using for loop to remove duplicates
    for i in list_a:
        if i not in new_list:
            new_list.append(i)
    print(new_list)    
remove_duplicates()

def remove_dup_set():   # using sets to remove duplicates
    return list(set(list_a))

print(remove_dup_set())
    
    
    
# write a function that returns a sentence with its characters in reverse oder
# used 5 diffrrenr options to solve this question 

def reverse_sentence(words): # using string and split 
    split_word = words.split()
    join_word = " ".join(split_word[::-1])
    return join_word
print(reverse_sentence("This is reversed"))

def word_join(x):   #using one lineer killer 
    return " ".join(x.split()[::-1])

print(word_join("This is owen testing"))

def word_reversedby(y): # using reversed keyword
    w = y.split()
    return " ".join(reversed(w))
print(word_reversedby("using reversed key word"))

def word_split_join(w):
    w_split = w.split()
    w_split.reverse()
    return " ".join(w_split)
print(word_split_join("This is reversed too"))



# create a password generator using randome char 
# you can use Strinf, choces and random to generate the values
# you can use string constance and operations to deal with this.
import string
import random

def password_generator():
    set_combine1 = string.ascii_letters
    set_combine3 = string.digits
    set_combine4 = string.punctuation
    
    all_combination = set_combine1  + set_combine3 + set_combine4
    password = "".join(random.choices(all_combination,k=8))
    
    return password
print(password_generator())

# use one function to return the password generator using choice
def psd_gen(size=9, combination = string.ascii_letters + string.digits + string.punctuation):
    return ("".join(random.choice(combination) for _ in range(size)))
print(psd_gen(int(input("How many char is your passwd? : "))))



# Use the requests library to load the HTML of the page into Python
# Set up BeautifulSoup to process the HTML
# Find out which HTML tags contain all the titles
# Use BeautifulSoup to extract all the titles from the HTML
# Format them nicely



base_url = "http://www.nytimes.com"
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", "").strip())
    else:
        print(story_heading.contents[0].strip())
        

        
# Fibonacci number generation:
# using if condition to loop thru fibonacci
def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())


# computer game guess(user keeps guess number and the computer tries to guess)
def guessing_game():
    high_range = int(input("What is the number range?\n1 to ..."))
    low_range = 1
    midpoint = int(high_range / 2)
    guess_count = 0

    while True:
        print(f"Is your number {midpoint}?\n1. Yes\n2. Too low\n3. Too high")
        guess = int(input())
        if guess == 1: # If the guess is correct
            print(f"I got it in {guess_count + 1} tries!")
            break
        elif guess == 2: # If the guess is too low
            guess_count += 1
            low_range = midpoint
            midpoint = low_range + int(((high_range - low_range) / 2))
        else: # if guess is too high
            guess_count += 1
            high_range = midpoint
            midpoint = low_range + int(((high_range - low_range) / 2))

    print("Thanks for playing!")
(guessing_game())


# 

def solutionA():
    user_array = [1,3,5,7,2]
    for x in range (min(user_array), max(user_array)):
        if x not in user_array:
            break
        return x
# print(solutionA())

from itertools import count, filterfalse # ifilterfalse on py2

def solution(A): 
    print(next(filterfalse(set(A).__contains__, count(1))))
solution(A=[3,-2,5,7])


#create a simple tic tac toe game:
# tell the user if there is a winn, 
# whre there is 0 -> mean no player has played
# use 1 and 2 as your computer and player


import numpy
game = [
[2,2,1],
[1,1,2],
[1,2,1]]
set_r = ()
set_c = ()
def line_match(game):
	for i in range(3):
		set_r = set(game[i])
		if len(set_r) == 1 and game[i][0] != 0:
			return game[i][0]
	return 0
#transposed column function for future use
#def column(game):
#	trans = numpy.transpose(game)
#	for i in range(3):
#		set_r = set(trans[i])
#		if len(set_r) == 1 and trans[i][0] != 0:
#			return list(set_r)[0]

def diagonal_match(game):
	if game[1][1] != 0:
		if game[1][1] == game[0][0] == game[2][2]: 
			return game[1][1]
		elif game[1][1] == game[0][2] == game[2][0]:
			return game[1][1]			
	return 0
if line_match(game) > 0:			
	print (str(line_match(game)) + str(" row wins!"))
if line_match(numpy.transpose(game)) > 0:
	print (str(line_match(numpy.transpose(game))) + str(" column wins!"))
if diagonal_match(game) > 0:
	print (str(diagonal_match(game)) + str(" diagonal wins!"))


# soln 2

def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(checkGrid(also_no_winner))