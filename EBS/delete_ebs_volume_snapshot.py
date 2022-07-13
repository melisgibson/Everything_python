import boto3

# deletes a snapshot 

ec2 = boto3.client('ec2')

response = ec2.delete_snapshot(SnapshotId='snap-0051252d3daaa208b')

print(response)
