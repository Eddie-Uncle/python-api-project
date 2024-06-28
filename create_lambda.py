import boto3
import json

# Initialize the Boto3 client
client = boto3.client('lambda')

# Define the function parameters
function_name = 'hello_lambda'
runtime = 'python3.12'
role = 'arn:aws:iam::account_id:role/lambda_role'
handler = 'lambda_function.lambda_handler'
zip_file_path = 'function.zip'

# Read the zip file
with open(zip_file_path, 'rb') as f:
    zip_file_content = f.read()

# Create the Lambda function
response = client.create_function(
    FunctionName=function_name,
    Runtime=runtime,
    Role=role,
    Handler=handler,
    Code={'ZipFile': zip_file_content},
    Description='My Lambda function',
    Timeout=15,
    MemorySize=128,
    Publish=True
)

print(json.dumps(response, indent=4))

