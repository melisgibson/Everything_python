import boto3

# lists objects in S3 bucket

s3 = boto3.client('s3')
response = s3.list_objects(Bucket = "mypythonpractice2")["Contents"]
objects = response
print(len(objects)) # gives number of objects in bucket
for object in objects:
    print(object["Key"]) # prints the object key
   