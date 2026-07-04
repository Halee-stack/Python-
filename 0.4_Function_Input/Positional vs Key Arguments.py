# Functions with input

# We can also have multiple inputs too which can be written by separating with commas.
# Keyword arguments are arguments that you pass to a function by specifying the parameter name. This makes it clear which value belongs to which parameter.

#def greet_with_name(name):
    #print(f"Hello {name}")
    #print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")
#functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#greet_with("kate", "Brooklyn")
#greet_with("brooklyn", "kate")
greet_with(name="Kate", location="Brooklyn")