# write a funtion that will retrun a list not containing duplicates.

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
    