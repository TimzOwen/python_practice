def guessing_game():
    high_range = int(input("What is the number range?\n1 to ..."))
    low_range = 1
    midpoint = int(high_range / 2)
    guess_count = 0

    while True:
        print(f"Is your number {midpoint}?\n1. Yes\n2. Too low\n3. Too high")
        guess = int(input())
        if guess == 1: # If the guess is correct
            print(f"I got it in {guess_count + 1} tries!")
            break
        elif guess == 2: # If the guess is too low
            guess_count += 1
            low_range = midpoint
            midpoint = low_range + int(((high_range - low_range) / 2))
        else: # if guess is too high
            guess_count += 1
            high_range = midpoint
            midpoint = low_range + int(((high_range - low_range) / 2))

    print("Thanks for playing!")
(guessing_game())