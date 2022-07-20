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
    