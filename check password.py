correct_password = "SecretPassword123"
attempts_left = 3

while attempts_left > 0:
    guess = input("Enter your password: ")
    
    if guess == correct_password:
        print("Access Granted")
        break
    else:
        attempts_left -= 1
        
        if attempts_left > 0:
            print(f"Incorrect password. Remaining attempts: {attempts_left}")
        else:
            print("Account Locked")
