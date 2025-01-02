# Sentiment Analysis Step Functions

This project provides a serverless sentiment analysis pipeline using AWS Step Functions, Lambda, and DynamoDB. It processes customer review data from an S3 bucket, analyzes sentiment, and stores the results in DynamoDB.

## Features:
- **Sentiment analysis** for customer reviews.
- **AWS Step Functions** orchestrate the workflow.
- **Lambda functions** handle review extraction, sentiment analysis, and result storage.
- **S3 trigger** automatically processes reviews as they are uploaded to the S3 bucket.

## Architecture Overview:
- **ExtractFeedback**: Extracts feedback data from the S3 event or DynamoDB.
- **AnalyzeSentiment**: Performs sentiment analysis on the extracted feedback.
- **StoreResults**: Stores the sentiment analysis results in DynamoDB.
- **State Machine**: Orchestrates the entire process using AWS Step Functions.

## Setup

### Prerequisites:
- **Serverless Framework** installed.
- AWS CLI configured with appropriate credentials.

### Deploy:
1. Clone this repository.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Deploy the service to AWS:
   ```bash
   serverless deploy
   ```

## Resources:
- **DynamoDB Table**: Stores review data and sentiment analysis results.
- **IAM Roles**: Permissions for Lambda and Step Functions execution.
- **Cloudwatch**: Cloudwatch log group for a step function.
- **SNS**: SNS to send an email when negative sentiment detected.

## Samples:
In the reviews folder you can find a set of 10 files simutating rare workload, no more than 10 
feedbacks in one upload. Upload those files to s3 one by one to test the project.

## License
This project is licensed under the MIT License.