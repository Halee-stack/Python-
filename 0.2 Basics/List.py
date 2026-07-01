# LIST: A list in Python is a built-in data structure used to store multiple items in a single variable. Lists are ordered, mutable, and can contain different data types.

state_of_America = ["NY", "NJ", "PA", "MO","CA","VA", "TX"]
state_of_America[1] = "NC"

state_of_America.extend(["kt"])
print(state_of_America)

# it will print ['NY', 'NC', 'PA', 'MO', 'CA', 'VA', 'TX', 'kt']