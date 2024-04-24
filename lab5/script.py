import requests
import logging
import boto3
import os
from botocore.exceptions import ClientError

def download(url):
    r = requests.get(url)
    return r.text

def upload_to_s3(data, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.put_object(Body=data, Bucket=bucket, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

data = download("https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv")

bucket_name = "ist-grb-muhlemann-test"
object_name = "VQHA80.csv"

if upload_to_s3(data, bucket_name, object_name):
    print("File uploaded successfully to S3 bucket:", bucket_name)
else:
    print("Failed to upload file to S3 bucket")



