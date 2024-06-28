import boto3
import json

# Initialize the Boto3 clients
lambda_client = boto3.client('lambda')
apigateway_client = boto3.client('apigateway')

# Define the function and API parameters
function_name = 'hello_lambda'
api_name = 'MyAPI'
resource_path = 'hello'
region = 'us-east-1'  # Replace with your region
account_id = 'ACCOUNT_ID'  # Replace with your account ID

# Step 1: Create the API
api_response = apigateway_client.create_rest_api(
    name=api_name,
    description='My REST API'
)
api_id = api_response['id']
print(f"API ID: {api_id}")

# Step 2: Get the Root Resource ID
resources = apigateway_client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources['items'] if resource['path'] == '/'][0]['id']
print(f"Root Resource ID: {root_id}")

# Step 3: Create a Resource
resource_response = apigateway_client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart=resource_path
)
resource_id = resource_response['id']
print(f"Resource ID: {resource_id}")

# Step 4: Create a GET Method
apigateway_client.put_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

# Step 5: Integrate the Method with Lambda
lambda_arn = f"arn:aws:lambda:{region}:{account_id}:function:{function_name}"
apigateway_client.put_integration(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='GET',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri=f"arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/{lambda_arn}/invocations"
)

# Step 6: Add permission to Lambda for API Gateway
source_arn = f"arn:aws:execute-api:{region}:{account_id}:{api_id}/*/GET/{resource_path}"
lambda_client.add_permission(
    FunctionName=function_name,
    StatementId='APIGatewayAccess',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com',
    SourceArn=source_arn
)

# Step 7: Deploy the API
deployment_response = apigateway_client.create_deployment(
    restApiId=api_id,
    stageName='prod'
)
print(f"Deployment ID: {deployment_response['id']}")

# Step 8: Print the API URL
api_url = f"https://{api_id}.execute-api.{region}.amazonaws.com/prod/{resource_path}"
print(f"API URL: {api_url}")
