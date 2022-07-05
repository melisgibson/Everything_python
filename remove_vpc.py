import boto3

# deletes vpc

ec2 = boto3.client("ec2")

response = ec2.delete_vpc(VpcId="vpc-0fa856685aa3b26a1")

print(response)

# describes remaining vpcs

response = ec2.describe_vpcs()["Vpcs"]

vpcs = response

for vpc in vpcs:
    print(vpc["VpcId"])