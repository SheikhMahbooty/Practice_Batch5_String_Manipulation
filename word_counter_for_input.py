#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

#Input text
input_name = input("Enter your name: ")

#Splits the words by the spaces
word_split = input_name.split()

#Counts the words by the splits
word_count = len(word_split)

print("Number of words:", word_count)