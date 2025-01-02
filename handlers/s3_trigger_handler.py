import boto3
import os
import json

s3 = boto3.client('s3')
step_functions_client = boto3.client('stepfunctions')
STATE_MACHINE_ARN = os.environ['STATE_MACHINE_ARN']

def handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    file_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
    feedbacks = json.loads(file_obj['Body'].read().decode('utf-8'))

    if not isinstance(feedbacks, list):
        raise ValueError("Uploaded file must contain an array of feedbacks")

    for feedback in feedbacks:
        step_functions_client.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            input=json.dumps(feedback)
        )

    return {
        "statusCode": 200,
        "body": f"{len(feedbacks)} feedbacks triggered successfully"
    }
