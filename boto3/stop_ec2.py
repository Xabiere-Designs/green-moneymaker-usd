# Import the boto3 library for interacting with AWS services
import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define the tag to identify instances for stopping
dev_tag = {'Key': 'Environment', 'Value': 'Development'}

# Retrieve information about EC2 instances
response = ec2.describe_instances()

# Extract reservations from the response
reservations = response['Reservations']

# Iterate through each reservation
for reservation in reservations:
    # Extract instances from the reservation
    instances = reservation['Instances']

    # Iterate through each instance in the reservation
    for instance in instances:
        # Check if the dev_tag is present in the instance's tags
        # and if the instance is in the 'running' state
        if dev_tag in instance.get('Tags', []) and instance['State']['Name'] == 'running':
            # Print the instance ID
            print(instance['InstanceId'])
            
            # Stop the running instance
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
