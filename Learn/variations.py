# User input a message
message = input("Enter a message: ")

# prints the message in different variations
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

# splits up the words
words = message.split()
print("Words:", words)

# sorts first word and last word
sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0]) 
print("Alphabetic Last Word:", sorted_words[-1])
