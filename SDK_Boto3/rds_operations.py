#!/usr/bin/python
# Documentation source
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html
import boto3

client = boto3.client('rds')
instance_id = 'SPECIFY INSTANCE ID'

def list_rds():
    ###### List all instances and print defined information ######
    response = client.describe_db_instances()
    #print(response)
    for db in response['DBInstances']:
        print(
            "MasterUsername: {0}\nDBInstanceStatus: {1}\nDBInstanceIdentifier: {2}\nDBInstanceClass: {3}\nEngine: {4}\n".format(
            db['MasterUsername'], db['DBInstanceStatus'], db['DBInstanceIdentifier'], db['DBInstanceClass'], db['Engine']
            )
        )

def stop_rds_dynamicaly():
    ###### Stop all available instances ######
    response = client.describe_db_instances()
    for db in response['DBInstances']:
        if db['DBInstanceStatus'] == 'available':
            client.stop_db_instance(DBInstanceIdentifier=db['DBInstanceIdentifier'])

def start_rds(db_id):
    ###### Start instance by db_id ######
    client.start_db_instance(DBInstanceIdentifier=db_id)

def stop_rds(db_id):
    ###### Stop instance by db_id ######
    client.stop_db_instance(DBInstanceIdentifier=db_id)

def delete_rds(db_id):
    ###### Delete instance by db_id ######
    client.delete_db_instance(
        DBInstanceIdentifier=db_id,
        SkipFinalSnapshot=True
        )

list_rds()
#start_rds(instance_id)
#stop_rds(instance_id)
#stop_rds_dynamicaly()
#delete_rds(instance_id)