import boto3

# upload a file to an s3 bucket 

s3 = boto3.client('s3')
response = s3.upload_file( 
    Filename = 'newfile.txt', 
    Bucket = 'mypythonpractice2', 
    Key = 'newfile.txt')
    
response = s3.list_objects(Bucket = "mypythonpractice2")["Contents"] # sets the reponse to list the contents of the object in the bucket

objects = response

for object in objects:
    print(object["Key"]) # prints the object key
    

