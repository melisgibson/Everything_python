import boto3

# creates a vpc
ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('id')

response = ec2.create_vpc(CidrBlock='10.0.0.0/16')

print(response) 
