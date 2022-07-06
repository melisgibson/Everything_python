import boto3

# connect to dynamodb

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='xxxxxxxxxxxx',
    aws_secret_access_key='xxxxxxxxxxxxxxxx',
    )
    
    