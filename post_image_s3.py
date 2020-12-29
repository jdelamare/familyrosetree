import requests
import os
import logging
from utils.get_signed_url import create_presigned_post

def send_request(bucket_name, object_name, conditions, object_path=None):
    # Generate a presigned S3 POST URL
    response = create_presigned_post(bucket_name, object_name, conditions=conditions)
    if response is None:
        exit(1)

    # Demonstrate how another Python program can use the presigned URL to upload a file
    with open(object_path, 'rb') as f:
        files = {'file': (object_name, f)}
        http_response = requests.post(response['url'], data=response['fields'], files=files)
        print(http_response)
    # If successful, returns HTTP status code 204
    logging.info(f'File upload HTTP status code: {http_response.status_code}')