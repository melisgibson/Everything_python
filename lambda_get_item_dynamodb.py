import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
  client = boto3.resource('dynamodb', region_name='us-east-1')
  table = client.Table('Anime')   
  response =table.query(KeyConditionExpression=Key('episodes').eq(24))
  items=response['Items']
  print(items)
  return {
    'statusCode': 200,
    'body': items
  }