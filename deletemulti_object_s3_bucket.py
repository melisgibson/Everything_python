import boto3
import os
import glob

# delete multiple objects from s3 bucket
s3 = boto3.client("s3")
response = s3.list_objects(Bucket = "mypythonpractice2")["Contents"] # find all objects in bucket

objects = response
for object in objects:
    s3.delete_object(Bucket = "mypythonpractice2", Key = object['Key'])
    print(object["Key"])
