import boto3

# Create an SNS client
def send_sms(phone,message):
    client = boto3.client(
        "sns",
        aws_access_key_id="AKIAJQU4HOIVD2MPWU7Q",
        aws_secret_access_key="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",
        region_name="us-east-1"
    )
    client.set_sms_attributes(
        attributes={
           'DefaultSMSType': 'Transactional',
           'DefaultSenderID': 'VIN33T'
        }
    )
    # Send your sms message.
    response = client.publish(
        PhoneNumber = phone,
        Message = message
    )

    if response['ResponseMetadata']['HTTPStatusCode']==200:
        return True
    else:
        return False
