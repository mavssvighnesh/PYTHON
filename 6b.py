# Create a dictionary with the person's name and birthday.
birthday_dict = {"name": "John Doe", "birthday": "1980-01-01"}

# Split the birthday string into a list of components.
birthday_list = birthday_dict["birthday"].split("-")

# Join the birthday list into a single string.
birthday_string = "-".join(birthday_list)

# Print the birthday string.
print(birthday_string)