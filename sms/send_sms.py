import boto3

# Create an SNS client
def send_sms(phone,message):
    client = boto3.client(
        "sns",
        aws_access_key_id="AKIAI4PSHRG4CJSIJYAA",
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
