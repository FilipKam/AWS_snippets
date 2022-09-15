#!/usr/bin/python
# Documentation source
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
import boto3

ec2 = boto3.resource('ec2')
instance_id = ''

def list_all_instances():
    ###### List all instances ######
    for instance in ec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
            )
        )

def list_running_instances():
    ###### List only running instances ######
    for instance in ec2.instances.all():
        #if instance.state['Name'] == 'stopped':
        if instance.state['Name'] == 'running':
            print(instance.id, instance.instance_type, instance.state)

def stop_instances_dynamically():
    ###### Stop all running instances ######
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            instance.stop()

def start_instances_dynamically():
    ###### Start all stopped instances ######
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'stopped':
            instance.start()

def stop_instance(instance_id):
    ###### Stop instance by instance_id ######
    instance = ec2.Instance(instance_id)
    instance.stop()

def start_instance(instance_id):
    ###### Start instance by instance_id ######
    instance = ec2.Instance(instance_id)
    instance.start()

def terminate_instance(instance_id):
    ###### Terminate instance by instance_id ######
    instance = ec2.Instance(instance_id)
    instance.terminate()

#start_instance(instance_id)
#stop_instance(instance_id)
#terminate_instance(instance_id)
list_all_instances()