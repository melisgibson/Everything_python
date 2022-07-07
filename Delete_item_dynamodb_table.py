import boto3

dynamodb = boto3.resource('dynamodb', region_name= "us-east-1")
table = dynamodb.Table('Anime') 
# Delete item
response = table.delete_item(Key = {'episodes': 24, 'title': 'Parasyte'}) # Item Key

print(response)