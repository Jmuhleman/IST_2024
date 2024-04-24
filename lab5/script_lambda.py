import boto3
import urllib3
import logging
from datetime import datetime
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    def download(url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        return r.data

    # Function to upload data to an S3 bucket
    def upload_to_s3(data, bucket, object_name):
        s3_client = boto3.client('s3')
        try:
            s3_client.put_object(Body=data, Bucket=bucket, Key=object_name)
            return True
        except ClientError as e:
            logging.error(e)
            return False

    # Download the data
    data_url = "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv"
    data = download(data_url)

    # Generate the ISO 8601 timestamp
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

    # Create a new object name with the timestamp
    bucket_name = "meteo-grb-muhlemann-butty"
    original_object_name = "VQHA80.csv"
    object_name_with_timestamp = f"{original_object_name.split('.')[0]}-{timestamp}.csv"

    # Upload to S3
    if upload_to_s3(data, bucket_name, object_name_with_timestamp):
        return {
            "statusCode": 200,
            "body": f"File uploaded successfully to S3 bucket: {bucket_name} with filename {object_name_with_timestamp}"
        }
    else:
        return {
            "statusCode": 500,
            "body": "Failed to upload file to S3 bucket"
        }
