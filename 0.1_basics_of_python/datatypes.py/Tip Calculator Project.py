# Tip calculator Project
# 150 total bill

# 12 / 100 = 0.12 %
print("Welcome to the tip calculator!")
print(150 * 0.12) # 150 and on top 0.12 tip which is 18.0
# 150 + 0.12 = 18.0 ... 18.0 + 150 = $ 168
print(150 * 0.12 + 150)
# there is other way to do this 150 plus 1.12.... where 1 is 150 and .12 is 0.12...see the example below
print(150 * 1.12) # you will see floating decimals number too... so don't worry   168. 00 (1.__)
print(150 * 1.12 / 5) # divided in how many people. = 33.600
print(round(150 * 1.12 / 5)) # That is how you round numbers

# PROJECT
print("Welcome to the tip calculator!")
bill = (float(input("What was the total bil? $")))
# The variable is bill so now this bill is going to have a data types of a string. <class 'str'>
# So if I go ahead and hit run and let's just type some numbers in here, you'll see that the data type
# of the bill is, as we said, a string.
# turn type into float on line number 17
# In order to be able to do maths, you might remember we have to change this into a number format.So a float or an int.
# Now in this case, because the bill is likely to have numbers after the decimal place, it's probably better that we
# turn it into a float so that we get the most accurate result possible.
tip = int(input("What percentage tip would you like to give? 10 12 15 ")) #Dont write percentage sign.
people = int(input("How many people to split the bill? "))

# So now that we've got all the data collected from the user, we're finally ready to do some math.
bill_with_tip = tip / 100 * bill + bill #(original bill)
#bill_with_tip = bill * (1 + tip / 100) other way to get to the answer

print(bill_with_tip) #work on it and finish the project
