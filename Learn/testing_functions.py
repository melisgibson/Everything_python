# Write a 'split_name' function that takes a string and returns a dictionary with first_name and last_name
def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }

assert split_name("Harry Potter") == {
    "first_name": "Harry",
    "last_name": "Potter",
}, f"Expected {{'first_name': 'Harry', 'last_name': 'Potter'}} but received {split_name('Harry Potter')}"

# Ensure that 'split_name' can handle multi-word last names
assert split_name("Albus Wulfric Dumbledore") == {
    "first_name": "Albus",
    "last_name": "Wulfric Dumbledore",
}, f"Expected {{'first_name': 'Albus', 'last_name': 'Wulfric Dumbledore'}} but received {split_name('Victor Von Doom')}"

# Write an 'is_palindrome' function to check if a string is a palindrome (reads the same from left-to-right)
def is_palindrome(item):
    item = str(item)
    return item == item[::-1]
assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# Make 'is_palindrome work with numbers'
assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# Write a 'build_list' function that takes an item and a number to include in a list
def build_list(item, count = 1):
    items = []
    for _ in range(count):
        items.append(item)
    return items
assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"
