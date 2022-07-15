import boto3
import json
import random
import string

def lambda_handler(event, context):

    num = string.digits
    random_num = ( ''.join(random.choice(num) for i in range(10)))
    message = "You are user: "+str(random_num)
    
    sqs = boto3.client('sqs')
    
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/027427181034/random-num-queue",
        MessageBody=random_num)

    return {
        'statusCode': 200,
        'body': json.dumps(message)
        }