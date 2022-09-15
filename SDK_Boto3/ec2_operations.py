#!/usr/bin/python
# Documentation source
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
import boto3

client = boto3.resource('ec2')

#list all instances
def list_all_instances():
    for instance in client.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
            )
        )

# list only running instances
def list_running_instances():
    for instance in client.instances.all():
        #if instance.state['Name'] == 'stopped':
        if instance.state['Name'] == 'running':
            print(instance.id, instance.instance_type, instance.state)

# stop instances
def stop_instances():
    for instance in client.instances.all():
        if instance.state['Name'] == 'running':
            instance.stop()

# start instances
def start_instances():
    for instance in client.instances.all():
        if instance.state['Name'] == 'stopped':
            instance.start()

list_all_instances()