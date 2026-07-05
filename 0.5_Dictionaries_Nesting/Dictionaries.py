# A dictionary is one of Python's most powerful data structures. It stores data as key-value pairs, allowing you to quickly look up, add, update, and remove data using a key instead of a numeric index.
# Keys must be unique and values can repeat.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
##print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}
#wipe an existing dictionary

#programming_dictionary = {}
#print(programming_dictionary)

# edit an item in a dictionary
#programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
