# Set the emails variable to be an empty dictionary
emails = {}
print(emails)

# Add names to the emails dictionary without reassigning the variable.
emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@examples.com'
print(emails)

# Remove 'craig' from the emails dictionary w/o reassigning the variable
del emails['craig']
# Add 'dalton' to the emails dictionary
emails['dalton'] = 'dalton@example.com'
print(emails)

# Return a list of keys from the emails dictionary as 'users'
users = list(emails.keys())
print(users)

# Return a list of values from the emails dictionary as 'email list'
email_list = list(emails.values())
print(email_list)

# Return a list of tuples called 'pairs' representing the key/value pairs in 'emails'.
pairs = list(emails.items())
print(pairs)