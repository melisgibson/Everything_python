import boto3

# lists running EC2 instance IDs

ec2 = boto3.client("ec2")

response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance['State']['Name'] == 'running':
           ID = (instance["InstanceId"])
           print (ID)