# Lambda Function Deployment with API Gateway

## Introduction
This project demonstrates how to deploy an AWS Lambda function and expose it through an API Gateway using Python scripts.

## Prerequisites
- AWS CLI installed and configured
- AWS Role with permissions to create Lambda functions and API Gateway
- Python 3.x
- Required Python libraries: requirements.txt

## Setup and Configuration
### AWS CLI and Credentials
1. Install AWS CLI: [Installation guide](https://aws.amazon.com/cli/)
2. Configure AWS credentials:


### Python Environment
1. Install required libraries:
   1. boto3
   2. requests
   3. json
2. Create a Python script to deploy the Lambda function and API Gateway.
3. Create a Python script to test the API Gateway.

## Deployment
1. Run the deployment script to deploy the Lambda function and API Gateway.
2. Test the API Gateway using the test script.
3. Monitor the API Gateway and Lambda function in the AWS Management Console.

Test the Lambda function by invoking it directly using the AWS CLI or the AWS Management Console or using the test_api.py script.


### API Gateway
1. After deploying the Lambda function, run `create_api.py` to set up the API Gateway:

## Usage
To invoke the Lambda function via the API Gateway, send a request to the API endpoint:

## Conclusion
This project demonstrates how to deploy an AWS Lambda function and expose it through an API Gateway using Python scripts. This setup allows for easy deployment and testing of serverless applications on AWS.