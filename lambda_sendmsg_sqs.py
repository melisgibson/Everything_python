import boto3
import json
import random
import string


random_num = string.digits
print ( ''.join(random.choice(random_num) for i in range(10)))