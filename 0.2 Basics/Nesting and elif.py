print("Welcome to the Ferris wheel!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the Ferris wheel")
    age = int(input("What is your age?"))

    if age <= 12:
        print("pay $6 ticket.") # these 2 statement 12-18 comes under elif
    elif age <= 18:
        print("please pay $7 ticket.")
    elif age <= 22:
        print("pay $10 ticket") # elif condition  age range between 18-22
    elif age <=30:
        print("please pay $11 ticket")
    else:
        print("please pay $12 ticket")
else:
    print("Sorry, you cannot ride the Ferris wheel.")
