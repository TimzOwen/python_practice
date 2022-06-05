# function 
def greeting_message(school,name):
    print(f"from of {school} we welcome home Engineer {name}") 

greeting_message("set","Timz")


# LISTS

mylist = ["one","two","three","Four"]
mysecond_data = ["Timz"] * 5

a,b = 4, 8 # simultaneous assignments

# iterate lists 

mydata = ["one","Two","three","Four","Five","six"]
for data in mydata:
    print(data)

print(mydata[0]) # access the first index
print(mydata[-2]) # access second last item
print(mydata[-1]) # access last item
#check elements availabilitu
if "one" in mydata:
    print("yes")
else:
    print("No")

print(len(mydata)) # get total number of elements in a list

mydata.append("seven") #add elements in a list

mydata[0] = "eight" #add at specific index

mydata.pop() # remove last element in a list

mydata.clear() # remove all elements in a list

mydata.reverse() # Reverse elements in a list 

mydata.sort() # sort data in a list

print(mysecond_data + mydata) # list concatenation

mysecond_data = mydata  # copy data into new list[modifies both lists]
mysecond_data.append("twenty")

new_data = mydata.copy() # copying to new list but does not modify both

print(mydata[3:]) # string clicing


print([i*i for i in mydata]) # string comprehension 
print(mydata)





# TUPLES
# ordered immutable elements in branckets.(single items must be comma separated) 

my_tuples = ("one",2, 4, "seven",2,3,4,6,7,8,9)  # tuple creation

my_tuple = ("Timz",) # returns a tuple
my_tuples = ("Timz") #returns a string object
 
list_to_tuple = (["one","Two","Three"]) # returns a type list
list_2_tuple = tuple(list_to_tuple) # returns a type of tuple

list_to_tuple[0] # accessing tuples at specific index

for items in my_tuples:  # Itereate throu elements in tuples
    print(items)

if "one" in my_tuples:  # Check elements availability on a tuple
    print("yes")
else:
    print("No")

len(my_tuples) # returns total number of items in the a tuple

my_tuples.count(2) # returns the total number of occurance of element in tuple

my_tuples.index(2) # returns first occurrance of element in multiple occurance

tuple_to_list = list(my_tuples) # convert tulpe to list

back_to_tuple = tuple(tuple_to_list) # back to tuple from list 

my_tuples[::2] # print in intervals of 2
reversed(my_tuple) # reverse a tuple in python
my_tuples[1:2] # print elements between 1 and 2
my_tuples[::-2] # prints at inteval from last element

for x in reversed_tuple: # retuens a list of reversed tuple
    print(x)

# unpack elements from a tuple
unpack_tuples = ("Timz", 20, "Developer") 

user_name, age, role = unpack_tuples
print(user_name)
print(age)
print(role)

# compare lists and tuple in time and space complexity (tuples safes on space and time than list)
import sys
import timeit

my_list = [0,1,2,3,4,5,6,7,8,9]
my_tuple = (0,1,2,3,4,5,6,7,8,9)

print(sys.getsizeof(my_list)) # returns 152
print(sys.getsizeof(my_tuple)) # returns 125
print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=10000000)) #0.6379658329997255
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=10000000)) #0.11949894600002153






# DICTIONARIES
# unordered, mutable,key-value items

my_dictionary = {"name":"Timz","age":22,"Role":"Developer"} # create a dictionaty
my_dictionary2 = dict(user="Owen",staff="Engineer",laptop="HP") # second dictionary
 
my_dict_fun = dict(city="Nairobi", population=400, senetor="Sonko") # creating using dictinary function

my_dictionary["name"] # access elements in a dic

my_dictionary["car"] = "BMW" # adding new elements

del my_dictionary["age"] # delete items in the dict

my_dictionary.pop("age") # remove specific index 

my_dictionary.popitem() # removes last item in the dictonary


if "name" in my_dictionary: # check element occurance in dictionary
    print("present")
else:
    print("No such key")


for key,value in my_dictionary.items(): # loop thru key and value pairs dict
    print(key,value)


try:
    print(my_dictionary["car"]) # searching an element using try-except
except:
    print("No such elemeny")


my_dictionary.update(my_dictionary2) # merging two dictionaries




        
# SETS 
# unordered, nutable ,non-repetitive items

set_items = {2,4,6,8,10} # create new set

for x in set_items: # Iterate thru a set
    print(x)


