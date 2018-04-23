import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-6871a115',
    InstanceType='t2.micro',
    # BlockDeviceMappings=[
    #     {
    #         'DeviceName': '/dev/sda1',
    #         'Ebs': {
    #             'Encrypted': False,
    #             'DeleteOnTermination': True,
    #             'VolumeSize': 10,
    #             'VolumeType': 'gp2'
    #         },
    #     },
    # ],
    MinCount = 1,
    MaxCount = 1,
)