import json
import boto3
import os

DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    table = dynamodb.Table(DYNAMODB_TABLE)

    feedback = event
    table.put_item(
        Item={
            'feedbackId': feedback['feedbackId'],
            'feedbackText': feedback['feedbackText'],
            'feedbackCategory': feedback['feedbackCategory'],
            'timestamp': feedback['timestamp'],
            'processed': False
        }
    )

    return {
        'feedbackId': feedback['feedbackId'],
        'feedbackText': feedback['feedbackText']
    }
