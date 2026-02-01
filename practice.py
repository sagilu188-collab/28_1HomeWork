tries = 0
maxTries = 5
password = int(input("Enter Password:"))

while True:
    cPassword = int(input("Confirm password:"))
    if password == cPassword:
        print("Password Accepted")
        break

    else:
        tries += 1
        if tries >= maxTries:
            print("Access Denied")
            break

print("Number of tries:", tries)
