import json
import os
import boto3

comprehend = boto3.client('comprehend')

def handler(event, context):
    feedback_id = event['feedbackId']
    feedback_text = event['feedbackText']
    
    try:
        response = comprehend.detect_sentiment(
            Text=feedback_text,
            LanguageCode='en'
        )
        sentiment = response['Sentiment']  # Sentiment result (POSITIVE, NEGATIVE, NEUTRAL, MIXED)

    except Exception as e:
        sentiment = 'UNKNOWN'
        print(f"Error calling AWS Comprehend: {str(e)}")
    
    return {
        'feedbackId': feedback_id,
        'sentiment': sentiment
    }

