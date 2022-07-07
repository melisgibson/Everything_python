import boto3

client = boto3.client('dynamodb', region_name= "us-east-1")

try:
    resp = client.delete_table(
        TableName="Anime", # Table name
    )
    print("Table was deleted successfully!")
except Exception as e:
    print("Error deleting table:")
    print(e)