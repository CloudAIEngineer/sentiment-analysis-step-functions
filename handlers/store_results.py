import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    feedback_id = event['feedbackId']
    sentiment = event['sentiment']
    
    table = dynamodb.Table(DYNAMODB_TABLE)
    table.update_item(
        Key={'feedbackId': feedback_id},
        UpdateExpression="SET sentiment = :sentiment, #processed = :processed",
        ExpressionAttributeValues={
            ':sentiment': sentiment,
            ':processed': True
        },
        ExpressionAttributeNames={
            '#processed': 'processed'
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Sentiment result stored for {feedback_id}")
    }
