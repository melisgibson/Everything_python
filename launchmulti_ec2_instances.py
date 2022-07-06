import boto3

# Launch multiple EC2 Instances

ec2 = boto3.resource("ec2")

response = ec2.create_instances(ImageId = 'ami-0cff7528ff583bf9a',
    InstanceType = 't2.micro',
    MaxCount = 2,
    MinCount = 2)
    
print(response) 