users = []

# add users to list with append
users.append('kevin')
users.append('bob')
users.append('alice')
print(users)

# remove 'bob' from list
del users[1]
print(users)

# reverse list assigned to 'reverse_users' list
rev_users = list(reversed(users))
print(rev_users)

# add user 'melody' to where 'bob'
users.insert(1, 'melody')
print(users)

# add users 'andy', 'wanda', and 'jim' with single command
users += ['andy', 'wanda', 'jim']
print(users)
 
# slice the users list to return the 3rd and 4th items, assign result to 'center_users'
center_users = users[2:4]
print(center_users)