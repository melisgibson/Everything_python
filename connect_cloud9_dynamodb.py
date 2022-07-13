import boto3

# Connect to dynamodb

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='******', # Input access key id
    aws_secret_access_key='*****', # Input secret key
    )
    
