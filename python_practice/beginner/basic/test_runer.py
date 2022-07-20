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