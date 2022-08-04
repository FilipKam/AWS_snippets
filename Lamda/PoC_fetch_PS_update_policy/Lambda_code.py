import boto3
import json

bucket_name = ''
parameter_name = ''
local_bucket_policy = 'bucket_policy.json'

def lambda_handler(event, context):
    account_ids = fetch_ssm_parameter(parameter_name) # fetch account ids from ssm parameter
    account_arns = format_user_arn(account_ids) # formate the account ids into arn format
    bucket_policy = update_bucket_policy(account_arns)
    update_s3_policy(bucket_policy) # update the s3 policy with new account ids


def fetch_ssm_parameter(parameter_name):
    ###### Fetch parameter from SSM. Return comma delimited string. ######
    ssm_client = boto3.client('ssm') # initialize ssm client
    parameter = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    return parameter ['Parameter']['Value']

def format_user_arn(account_id):
    ###### Format account IDs into arn. Return list of arns. ######
    user_arn = []
    account_id_list = account_id.split(',')
    for id in account_id_list:
        user_arn.append('arn:aws:iam::{}:root'.format(id))
    return user_arn

def update_bucket_policy(account_arns):
    ###### Update S3 policy with new account ids. ######
    bucket_policy = load_json()
    for arn in account_arns:
        bucket_policy["Statement"][0]["Principal"]["AWS"].append(arn)
    return json.dumps(bucket_policy)

def load_json():
    ###### Load JSON file and return it as a object. ######
    f = open(local_bucket_policy, 'r')
    data = json.load(f)
    f.close()
    return data

def update_s3_policy(bucket_policy):
    ###### Load S3 policy and return it as a object. ######
    s3_client = boto3.client('s3') # initialize s3 client
    s3_client.put_bucket_policy(
        Bucket=bucket_name,
        Policy=bucket_policy
    )
    