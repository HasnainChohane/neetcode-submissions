#Stored credentials
username = "admin"
password = "1234"
#input variables for testing
user1, pass1 = "admin", "1234"    
user2, pass2 = "admin", "4321"    
user3, pass3 = "user", "1234"     
#reate attempts counter
attempts = 3
print("Starting attempts:", attempts)

#Run 1
input_user = user1
input_pass = pass1
#Check with logical 'and'
is_logged_in = input_user == username and input_pass == password
#Print result
print("Run 1 -> Login:", is_logged_in)
#Reduce attempts by 1
attempts -= 1
#Print updated attempts
print("Attempts left:", attempts)


# Run 2
input_user = user2
input_pass = pass2
is_logged_in = input_user == username and input_pass == password
print("Run 2 -> Login:", is_logged_in)
attempts -= 1
print("Attempts left:", attempts)

# Run 3
input_user = user3
input_pass = pass3
is_logged_in = input_user == username and input_pass == password
print("Run 3 -> Login:", is_logged_in)
attempts -= 1
print("Attempts left:", attempts)