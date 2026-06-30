print("Welcome to the Ferris wheel!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the Ferris wheel")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    wants_photo = input("Do you want photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        # Add $3 to their bill.
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you cannot ride the Ferris wheel.")
