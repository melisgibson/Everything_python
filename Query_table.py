import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Anime')    # Input table name  
response = table.query(
    KeyConditionExpression=Key('episodes').eq(24) # Input key to query
)

print(response)
