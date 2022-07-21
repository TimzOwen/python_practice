# create a password generator using randome char 
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