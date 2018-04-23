import boto3

client = boto3.client('route53')

response = client.create_hosted_zone(
    Name= 'uta.com.',
    CallerReference='20180417'
)
id = response['HostedZone']['Id']
response = client.change_resource_record_sets(
    HostedZoneId=id,
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'www.uta.com.',
                    'Type': 'A',  
                    'TTL':300,                  
                    'ResourceRecords': [
                        {
                            'Value': '192.168.1.1'
                        },
                    ],                                
                }
            },
        ]
    }
)