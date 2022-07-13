# user input name
Name = input("What is your name? ")
# user input age
Age = int(input("How old are you today? "))
# user enter favorite color
Favorite = input("Favorite color: ")
print(Favorite) # prints the value typed in for Favorite color

#print the lines with input values on multiple lines
print(Name)
print("is " + str(Age) + " years old")
print("and loves the color " + Favorite + ".")

# print the lines with input values, prints to one line
print(Name, end=" ")
print("is " + str(Age) + " years old", end=" ")
print("and loves the color " + Favorite + ".", end=" ")

# print the line with input values
print(Name, 'is', Age, 'years old and loves the color', Favorite + '.')
