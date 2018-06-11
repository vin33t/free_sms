import boto3

# Create an SNS client
def send_sms(phone,message):
    client = boto3.client(
        "sns",
        aws_access_key_id="AKIAJHQS7NNT6YUDC3LQ",
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
