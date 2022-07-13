import boto3

# deletes a single object from s3 bucket

s3 = boto3.client("s3")


response = s3.delete_object(Bucket = "mypythonpractice2", 
    Key = "db.py")

response = s3.list_objects(Bucket = "mypythonpractice2")["Contents"] # sets the reponse to list the contents of the object in the bucket

objects = response

for object in objects:
    print(object["Key"]) # prints the object key
