# function to choose between 3 greatest
def greatest_number(a,b,c):
    if a > b and a > c:
        print("a is greatest")
    elif b>a and b > c:
        print("b is greatest")
    else:
        print("c is greatest")
greatest_number(5,10,15)