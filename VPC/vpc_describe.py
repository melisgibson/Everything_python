import boto3

# describes one vpc based on vpc id

vpc = boto3.client('ec2')
vpicid = "vpc-0fa856685aa3b26a1"
response = vpc.describe_vpcs(
    VpcIds = [vpicid]
)
print(response)
