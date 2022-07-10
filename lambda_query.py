import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Anime')    # Input table name  

def lambda_handler(event, context):
  response = table.query(
    KeyConditionExpression=Key('episodes').eq(26) # Input key to query
)
  print("The query returned the following items:")
  for item in response['Items']:
    print(item)