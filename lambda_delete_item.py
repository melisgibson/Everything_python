import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
  dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
  table = dynamodb.Table('Anime')    # Input table name  

  try:
    response=table.delete_item(Key={'episodes':26, 'title':"Demon Slayer"})
    return "Done"
  except:
    raise