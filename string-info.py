# indexing and slicing
message = input("Enter a message: ") # user input message


print("First character:", message[0]) # prints the first character of the message
print("Last character:", message[-1]) # prints the last character of the message
print("Middle character:", message[int(len(message) / 2)]) # prints the middle character of the message

print("Even index characters:", message[0::2]) # prints even 
print("Odd index characters:", message[1::2]) # prints odd

print("Reversed message:", message[::-1]) # print the message in reverse