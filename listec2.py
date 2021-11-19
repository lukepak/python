import boto3

AWS_REGION = "us-east-2"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

for volume in ec2.volumes.all():
    print(volume)
