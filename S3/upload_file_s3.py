import boto3

# upload a file to an s3 bucket 

s3 = boto3.client('s3')
response = s3.upload_file( 
    Filename = 'newfile.txt', 
    Bucket = 'mypythonpractice2', 
    Key = 'newfile.txt')
    
