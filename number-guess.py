#Guess number
num = 20

while True:
    guess = int(input("Enter a number between 1 to 25: "))
    
    if guess == num:
        print("You Win!")
        break
    elif num > guess:
        print("You guessed lower number")
    else:
        print("You guessed higher number")
