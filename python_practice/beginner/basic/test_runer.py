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