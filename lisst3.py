import logging
import boto3
from botocore.excepytions import ClientError

s3 = boto3.client('s3')
response = s3.list_buckets()
print('Existing buckets:')
for bucket in reponse['Buckets']:
    print(f' {bucket["Name"]')
