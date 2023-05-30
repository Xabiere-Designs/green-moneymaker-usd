import boto3

instance_id = "i-0a6f988e70579814d"

ec2 = boto3.client('ec2')
   
response = ec2.stop_instances(
    InstanceIds=[
        instance_id
    ],
    
)    

print(response)
    

    
