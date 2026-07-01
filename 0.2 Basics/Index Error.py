#Index Error: It occurs when you try to access a list, tuple, or string using an index that doesn't exist.

fruits = ["apple", "banana", "orange", "mango", "pineapple"]
vegetables = ["Cauliflower", "Onion", "Cabbage", "Peas", "Eggplant"]
seasonal = [fruits, vegetables]
print(seasonal)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Radish", "Cucumber", "Carrots", "Tomatoes", "Potatoes"]

seasonal = [fruits, vegetables]
#fruits is on index 0 and vegetable is on index 1. nested within the nested list.
print(seasonal [0][2])