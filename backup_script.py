import boto3
from botocore.exceptions import ClientError
"Creating an S3 bucket in a specified region"
def create_bucket(bucket_name, region=None):
    try:
        s3_client = boto3.client('s3',region_name=region)
        if region:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        else:
            s3_client.create_bucket(Bucket=bucket_name)
        print(f'Bucket "{bucket_name}" created successfully. ')
    except ClientError as e:
        print(e)
        return False
    return True

def upload_file(file_name, bucket, object_name=None):
    "Uploading a file to an S3 bucket"
    try:
        s3_client = boto3.client('s3')
        if object_name is None:
            object_name = file_name
        s3_client.upload_file(file_name, bucket, object_name)
        print(f'File "{file_name}" uploaded to bucket "{bucket}" as "{object_name}".')
    except ClientError as e:
        print(e)
        return False
    return True

def list_files(bucket_name):
    "Listing all the files in an S3 bucket"
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print(f"Files in {bucket_name} :")
        for obj in response['Contents']:
            print(f"- {obj['Key']}")
    else:
        print(f"No files found in bucket {bucket_name}")

def download_file(bucket_name, object_name, file_name):
    "Downloading a file from S3 bucket"
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(bucket_name, object_name, file_name)
        print(f'File "{object_name}" downloaded from bucket "{bucket_name}" to "{file_name}". ')
    except ClientError as e:
        print(e)
        return False
    return True

def main():
    bucket_name = 'bucketuqfortest'
    region = 'ap-south-1'

    create_bucket(bucket_name, region)
    upload_file('/Users/abhishekkamal/desktop/aws/HomePage.png',bucket_name)

if __name__=="__main__":
    main()

