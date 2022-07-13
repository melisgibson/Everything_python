import boto3

# search s3 bucket

s3 = boto3.client('s3')
response = s3.list_buckets() # list buckets

buckets = response["Buckets"] 

for bucket in buckets:
    print(bucket["Name"]) 
    
print('\n') # prints a new line

# searches object in bucket

s3 = boto3.client('s3')
response = s3.list_objects(Bucket = "mypythonpractice2") # lists objects in bucket

print(response)
