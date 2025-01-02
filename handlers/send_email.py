import os
import boto3
import json

sns_client = boto3.client('sns')

def handler(event, context):
    feedback_id = event['feedbackId']
    feedback_text = event['feedbackText']

    # In a real business scenario, we would need to extract the customer's 
    # contact information using the Feedback ID.
    email_subject = f"Negative Sentiment Detected: Feedback ID {feedback_id}"
    email_body = (
        f"Dear Manager,\n\n"
        f"The sentiment analysis detected NEGATIVE sentiment.\n"
        f"Feedback ID: {feedback_id}\n"
        f"Message: {feedback_text}\n\n"
        f"Please review the issue.\n\n"
        f"Best regards,\n"
        f"Sentiment Analysis Team"
    )

    # Publish to SNS Topic
    sns_client.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Subject=email_subject,
        Message=email_body
    )

    return {}