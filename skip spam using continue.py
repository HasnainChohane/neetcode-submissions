#skip spam by using continue
users = ["alice ", "SPAM", "bob", "charlie", "SPAM", "davide"]

for user in users:
    if user == "SPAM":
        continue
    print(f"Sending email to: {user.strip()}")
