def format_name(f_name, l_name):
    formatted_f_name = (f_name.title())
    formatted_l_name = (l_name.title())

    return(f"{formatted_f_name} {formatted_l_name}")

print(format_name("kate", "jake"))


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hey"))
print(output)

# In Python, a function with output is a function that uses the return statement to send a value back to the caller.