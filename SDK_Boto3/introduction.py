#!/usr/bin/python
# Documentation source
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#using-boto3
    # https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session
    # https://towardsdatascience.com/introduction-to-pythons-boto3-c5ac2a86bb63

# update boto3 to the latest version
# pip install boto3 --upgrade

# check boto3 version
# pip show boto3

import boto3
bucket_name = 'sdk-workshop-147852'

##### Client interface #####
# The client interface is a low-level interface to AWS. It is the direct interface to AWS services. 1:1 mapping of API calls to methods.
# full coverage of AWS services

def client_introduction():
    client = boto3.client('s3')

    response = client.list_objects_v2(Bucket=bucket_name) # list all objects in the bucket
    #print(response)

    for content in response['Contents']:
        obj_dict = client.get_object(Bucket=bucket_name, Key=content['Key']) # get the object
        print(content['Key'], obj_dict['LastModified']) # print the object key and last modified date

##### Resource interface #####
# The resource interface is a higher-level interface to AWS. It abstracts away the low-level service API details from the user.
# All AWS services are NOT covered by the resource interface.

def resource_introduction():
    s3 = boto3.resource('s3')

    bucket = s3.Bucket(bucket_name) # get the bucket
    #print(bucket)

    #in this case you do not have to make a second API call to get the objects; they're available to you as a collection on the bucket.

    for obj in bucket.objects.all(): # list all objects in the bucket
        print(obj.key, obj.last_modified) # print the object key and last modified date

""" The available resources are:
   - cloudformation
   - cloudwatch
   - dynamodb
   - ec2
   - glacier
   - iam
   - opsworks
   - s3
   - sns
   - sqs """

######################################################################

#client_introduction()
resource_introduction()