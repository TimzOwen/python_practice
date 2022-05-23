# function 
def greeting_message(school,name):
    print(f"from of {school} we welcome home Engineer {name}") 

greeting_message("set","Timz")


# LISTS

mylist = ["one","two","three","Four"]
mysecond_data = ["Timz"] * 5

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

