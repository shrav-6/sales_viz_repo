import http.client
import boto3

def lambda_handler(event, context):
    github_file_url = '/shrav-6/sales_viz_repo/raw/master/lambda_function.zip'
    s3_bucket_name = "getuploadfromlambdamaybe"
    s3_key = "lambda_function.zip"

    # Extract host and path from the URL
    host = 'github.com'
    path = github_file_url

    # Establish connection to GitHub server using http.client
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path)
    response = conn.getresponse()

    if response.status == 200:
        file_content = response.read()  # Read response content
    else:
        print(f"Failed to download file: {response.status}")
        return

    # Upload file content to S3 bucket using boto3
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket_name, Key=s3_key, Body=file_content)
        print("File uploaded successfully to S3!")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
