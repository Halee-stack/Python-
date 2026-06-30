len("Hello") # whenever you see "" it is string
print(type(745878774)) # numbers have no "" so it's an integer... whole numbers
print(type("beautiful")) # so this is string... in string you can have both numbers and letters but make sure they have "".
print(type(2.167)) # decimal is Float
print(type(False)) # Boolean... no "" needed
print(type(True)) # Boolean... no "" needed


# TYPE CONVERSION
print(int("123") + int("456"))


name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int


print("Number of letters in your name: " + str(length_of_name))