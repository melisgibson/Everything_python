import boto3

# Connect to dynamodb

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAQMYWJSHVI5OBGKS6', # Input access key id
    aws_secret_access_key='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', # Input secret key
    )
    
