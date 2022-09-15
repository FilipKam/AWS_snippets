import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.resource('ec2')

def lambda_handler(event, context):
    ###### Called method on Lambda start ######
    logger.info('Lambda function started')
    list_all_instances()

def list_all_instances():
    ###### List all instances ######
    for instance in client.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
            )
        )