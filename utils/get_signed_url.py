import boto3
import os
import logging
from botocore.exceptions import ClientError

URL_EXPIRATION_SECONDS = 300

# def create_presigned_post():
def create_presigned_post(bucket_name, object_name,
                        fields=None, conditions=None, expiration=3600):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    session = boto3.Session(profile_name="familyrosetree")
    s3_client = session.client('s3')    # TODO: is it ok to use this in prod provided access key and secret access key are *secret* (session length?)

    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=None,
                                                     ExpiresIn=URL_EXPIRATION_SECONDS)
    except ClientError as e:
        logging.error(e)
        return None
    
    return response
