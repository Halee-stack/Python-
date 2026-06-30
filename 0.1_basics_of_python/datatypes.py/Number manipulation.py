# Floating and Rounding Number

# bmi formula = weight in kg / (Height in meter)^2


bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) # integer always round the whole number but in lowest... doesn't matter it will go above .5 ... it will still show the lowest number
print(round(bmi)) # as the decimal point reaches.5 it will round it to the highest number. READ THE DESCRIPTION
print(round(bmi, 2)) #And now when I hit Run, you'll see that this time, instead of simply rounding it to a whole number,
#it rounds it to a floating point number with two decimal places of accuracy.

# Assignment Operators
# Problem 1
score = 0
# User scores a point
score += 5
print(score)

# f-String
print("your score is " + str(score))

# Problem 2
score = 0 # integer
height = 1.8 # float
is_winning = True # boolean

# we will mix them all in to a sentence in a string and print it out by using f-string. (short for formatted string literal) and can add various values to the f-string.
print(f"your score is {score}, your height is {height}. You are winning is {is_winning}")
# So all of these different data types got combined into a string by using an f in front of the string,
# and then using these curly braces to place our variables into the string.
# By using f-strings, you cut down on a lot of the manual labor of inserting different data types into a string,