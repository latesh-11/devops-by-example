import boto3
import botocore.exceptions
import schedule
import time

def create_s3_bucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('your-bucket-name')

    try:
        response = bucket.create(
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-2'
            },
        )
        print(response)
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists and owned by you.")
        elif error_code == 'BucketAlreadyExists':
            print("Bucket already exists.")
        elif error_code == 'InvalidBucketName':
            print("Invalid bucket name.")
        else:
            print("Error creating bucket:", e)

# Schedule the task
schedule.every().day.at("01:00").do(create_s3_bucket)  # Change the time as per your requirement

# Main loop to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
