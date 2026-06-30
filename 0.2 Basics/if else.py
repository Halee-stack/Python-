print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
#All that I've got here is a print statement that says, "Welcome to the roller coaster!" as well as an
#input asking the user for their height in centimeters and then converting the string into a whole number,
#an integer, and then I'm storing it inside this variable called height

if height > 120:  # here colon goes after the if and its statement
    print("You can ride the rollercoaster")
    #else: # the indentation is very important in python. and in else statement you put colon
    print(
        "Sorry, you cannot ride the rollercoaster.")  # So the keywords if and else, as well as the colons that come after each of these lines.
# And finally also the indentation. Everything that is indented after the if is a block of code. So this is indented and it's effectively inside this if.
#So this line of code lives inside the else statement. This block of code lives inside the if statement. and if you mess up on the indentation, then you're
# probably going to get an IndentationError telling you that this line five probably should be indented.

