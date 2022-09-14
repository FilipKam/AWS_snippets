from http import client
#!/usr/bin/python

import boto3

client = boto3.resource('ec2')

#list all instances
for instance in client.instances.all():
     print(
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     )

# list only running instances
for instance in client.instances.all():
     if instance.state['Name'] == 'running':
         print(instance.id, instance.instance_type)