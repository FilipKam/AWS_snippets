#!/usr/bin/python
# Documentation source
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html
import boto3

client = boto3.resource('rds')

def list_rds():
    for rds in client.rds.all():
        print(rds)

list_rds()