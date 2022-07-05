import boto3

# describe all vpcs in account

import boto3

ec2 = boto3.client("ec2")


response = ec2.describe_vpcs()["Vpcs"]

vpcs = response

for vpc in vpcs:
    print(vpc["VpcId"])