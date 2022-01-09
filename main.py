import os
import logging
import boto3
from botocore.exceptions import ClientError
from PIL import Image
import smtplib
import imghdr
from email.message import EmailMessage
import hybrid



#upload
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3',aws_access_key_id='#####',aws_secret_access_key='#####')
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#menu
print ("Welcome to Sefy")
print ("# Press 1 to upload file")
print ("# Press 2 to download file")
print ("# other key to exit")
op=int(input())
if (op== 1):
    file_location=input("Enter file name with path: (with \\) ")
    buck=input("Enter the bucket name: ")
    obj=input("Enter the object name: ")
    hybrid.main()
    upload_file(file_location, buck, obj)
    print("DONE!")

elif (op==2):
    buck1= input("Enter bucket name :")
    obj1= input("Enter Object name: ")
    file1= input("Enter File name: ")
    s3 = boto3.client('s3',aws_access_key_id='######',aws_secret_access_key='######')
    s3.download_file(buck1, obj1, file1)
else:
    os._exit(0)

