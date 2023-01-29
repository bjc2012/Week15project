import boto3
import logging
import json
from datetime import datetime


def lambda_handler(event, context):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")

    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/358582585332/TheBlackSquad',
        MessageBody=current_time
    )
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }