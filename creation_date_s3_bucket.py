import boto3

# lists the creation date of an s3 bucket

s3 = boto3.client('s3')
response = s3.list_buckets() # list buckets

buckets = response["Buckets"] # set the variable "buckets" to respond with the list of buckets requested

for bucket in buckets: 
    print(bucket["CreationDate"]) # prints the creation date of each bucket within the variable "buckets".
