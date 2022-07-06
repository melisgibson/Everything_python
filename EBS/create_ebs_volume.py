import boto3

# creates an EBS volume

ec2 = boto3.client("ec2")

response = ec2.create_volume(AvailabilityZone='us-east-1f',
    Size=8,
    Encrypted=True,               
    VolumeType='gp2')

# describes EBS volumes and print Volume ID

response = ec2.describe_volumes()

volumes = response["Volumes"]

for volume in volumes:
  print(volume["VolumeId"])
