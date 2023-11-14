import boto3

# Create an EC2 resource
ec2 = boto3.resource('ec2')

# Create development instances
dev = ec2.create_instances(
    ImageId='ami-05c13eab67c5d8861',
    MaxCount=3,
    MinCount=3,
    InstanceType='t2.micro',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Development'},
                {'Key': 'Environment', 'Value': 'Development'}
            ]
        },
    ],
)

# Create production instances
prod = ec2.create_instances(
    ImageId='ami-05c13eab67c5d8861',
    MaxCount=1,
    MinCount=1,
    InstanceType='t2.micro',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Production'},
                {'Key': 'Environment', 'Value': 'Production'}
            ]
        },
    ],
)


