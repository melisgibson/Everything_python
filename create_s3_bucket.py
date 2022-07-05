import boto3

# creates a private s3 bucket

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("mypythonpractice2")

response = bucket.create(  
    ACL='private',
    
    
)

print(response)