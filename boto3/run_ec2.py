import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-06ca3ca175f37dd66',
    MaxCount=3,
    MinCount=3,
    InstanceType='t2.micro',
   )