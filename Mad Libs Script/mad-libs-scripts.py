# This is a Mad Libs script

# We can use the input function to prompt the user for input
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# We can use string formatting to insert the user's input into a string
story = "The {adj} {noun} {verb} over the lazy dog.".format(adj=adjective, noun=noun, verb=verb)

# We can use the print function to print the story to the console
print(story)
