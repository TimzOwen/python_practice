#user_credits = input(int("Enter amount to purchase"))
from curses import init_pair
import numbers


nairobi_grids = 2,4,6,8
for i in (nairobi_grids):
    print(i)
    
def safaricom_boosters(locatoion):
    for i in range(0,locatoion):
        print(f"users: {locatoion}")

#safaricom_boosters(5)

# create M-PESA API Daraja range users;

def mpesa_daraja(customers):
    number_users = int(input("Number os users in the system"))
    number_of_transactions = int(input("Enter range: "))
    
    while(number_users != number_of_transactions):
        print(f"number os users currently: {customers}")
        break # breaks out of the look when the nubmers are more than the customers
    
print(mpesa_daraja(50000000))

M_PESA_API = int(init_pair(2893))