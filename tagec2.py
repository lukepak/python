import boto3
AWS_REGION = "us-east-1"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

for volume in ec2_resource.volumes.filter(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'ebs-boto3',
                    ]
                }
            ]
        ):
    print(f'Volume {volume.id} ({volume.size} Gib) -> {volume.state}')
