# create a list of AWS services using python

# print empty list
services_list = []
print(services_list)

# populate list by adding items
services_list += ["EC2", "Lambda", "DynamoDB", "CloudFormation", "Cloud9", "S3"]
print(services_list)

# append item to the end of the list
services_list.append("Athena")
print(services_list)

# insert item into 2nd place on the list
services_list.insert(1, "CloudFront")
print(services_list)

# print length of the list
print(len(services_list))

# remove a service from the list by name
services_list.remove("DynamoDB")
print(services_list)

# remove a service from the list by index, the 4th item 
del services_list[3]
print(services_list)

# print the new list and the new length of the list
print(services_list)
print(len(services_list))

# print a sorted list
print(sorted(services_list))
