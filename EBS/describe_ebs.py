import boto3

# Describe EBS volume snapshot

ec2 = boto3.client('ec2')

response = ec2.describe_snapshots(SnapshotIds=["snap-0051252d3daaa208b"])

print(response)
