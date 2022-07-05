# f strings
firstname = "Melissa"
surname = "Gibson"

print(f"My first name is {firstname}. My family name is {surname}")

# number variables in strings
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

# create value in dictionary
user = {"first_name":"Ada"}
print(user)
{'first_name': 'Ada'}

# read value associated with key
user = {"first_name":"Ada"}
print(user["first_name"])

# update, add a key-value
user["family_name"] = "Byron"
print(user)

# delete a key-value pair
del user["family_name"]
print(user)

