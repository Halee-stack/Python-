#A docstring (documentation string) is a string placed at the beginning of a function, class, or module to describe what it does. It is enclosed in triple quotes (""" """ or ''' ''').


def format_name(f_name, l_name):
    """
      Formats a person's first and last names.

      Parameters:
          f_name (str): The first name.
          l_name (str): The last name.

      Returns:
          str: The full name with both names in title case.
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("Kate", "Jake")

length = len(formatted_name)
