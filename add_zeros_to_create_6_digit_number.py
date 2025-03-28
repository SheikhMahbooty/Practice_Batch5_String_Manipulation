# Prog02: Add leading zeros to create a 6-digit number

# Ask the user to input a number
number_input = input("Input: ")

# Format the number to add zeros to make 6 digits
modified_num = number_input.zfill(6)

# Print the formatted number
print("Output:", modified_num)
