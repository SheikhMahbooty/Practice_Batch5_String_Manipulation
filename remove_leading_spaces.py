# Prog01: Remove leading spaces from inputted name

# Ask the user to input their full name with spaces at the beginning
input_name = input("Input: ")

# Remove spaces 
stripped_name = input_name.lstrip()

# Print the cleaned name
print("output:", stripped_name)