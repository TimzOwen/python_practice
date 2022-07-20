# write a program that takes in first and last elements in a list

def list_comprehension():
    
    a = [2,4,6,8,10]
    b = []
    b.append(a[0])
    b.append(a[-1])

    print(b)

list_comprehension()

def list_comp(list_a):
    return [list_a[0], list_a[len(list_a) - 1]]
    
print(list_comp([2,3,4,4,5,6]))