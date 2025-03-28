#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#Input name
input_name = input("Enter your name: ")

#Remove the spaces and format text to lower text
snake_case = input_name.lower().replace(" ","_")

#Print modified name
print(snake_case)
