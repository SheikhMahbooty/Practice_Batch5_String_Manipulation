#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#Input name
input_name = input("Enter your name: ")

#Remove the spaces and format text to title text
pascal_case = input_name.title().replace(" ","")

#Print modified name
print(pascal_case)