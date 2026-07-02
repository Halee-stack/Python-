#range() is a built-in Python function that generates a sequence of numbers. 
# It is commonly used with a for loop to repeat a block of code a specified number of times. In range(1, 101), the sequence starts at 1 and ends at 100, because the second value (101) is excluded. During each iteration of the loop, the next number in the sequence is assigned to the loop variable until all numbers have been processed.

total = 0
for number  in range(1, 101):
    total += number
print(total)