import boto3
client = boto3.client('ec2')
snsClient = boto3.client('sns')

def lambda_handler(event,context):
    response = client.describe_addresses()
    eips = []
    for eip in response['Addresses']:
        if 'InstanceId' not in eip:
            eips.append(eip['PublicIp'])

    print(eips)

    # send email using sns
    if eips:
        snsClient.publish(
            TopicArn='paste ur arn here',
            Message = f"Unused eips are {str(eips)}",
            Subject = "Unused EIPS"
        )


# lambda_handler(None,None)
