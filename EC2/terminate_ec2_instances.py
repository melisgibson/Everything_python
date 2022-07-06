import boto3

# terminate all EC2 instances 

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

term = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
            term.append(instance['InstanceId'])

print(term)
print(ec2.terminate_instances(InstanceIds=(term)))
