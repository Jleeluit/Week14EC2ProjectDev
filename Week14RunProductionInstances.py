import boto3


ec2 = boto3.resource('ec2')

# create 3 intances for PROD
prod = ec2.create_instances(
    ImageId='ami-01a5f5bb7b408ee72',  #This AMI ID is from my AWS Cloud 9 IDE original EC2 AMI ID
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'Production'},
                {'Key': 'ENV','Value': 'Production'}
            ]
        }
    ]
)

print(prod)