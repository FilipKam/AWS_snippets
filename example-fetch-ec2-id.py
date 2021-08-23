# Essentially, there is no native way in the CDK to fetch instance id's and place them into an array for us to use in our template. Furthermore, it must be noted that the vpc.fromLookup [1] method does not exactly dynamically fetch "all of the vpc's" in your account as you still need to define some parameters in your code.

# With the above being said, because this is not possible using the CDK, there is a working around we can look at. For this work around, we can leverage any one of the AWS SDK's to obtain the EC2 instances in a given region, place them in an array, generate our template and launch our stack accordingly.

# While we do not in fact provide code support here at Premium Support, I have written out an example code for you in Python that demonstrates the above which I have attached to the case for your convenience. In my example code you will see the following:

# 	- Create an EC2 resource using Boto3 [2] where I obtain all the instance  id's in my given region and store the results in an array
# 	- Loop through the instance id's from the array we created above to generate the resources for our CloudFormation stack. To do this, I used the aws_cloudwatch.Alarm [3] resource in the CDK.

# When we run the "CDK synth" command on this implementation, the instance id's are retrieved and the template is generated accordingly. I have tested and validated this code example on my end and confirm that it does work as expected.

# To summarize your main concern, no we do not need to hardcode the EC2 instance values into our code as we can leverage an AWS SDK to get this information for us. If you would like to discuss this further, please feel free to reach out to me at any time as I will be more than happy to further assist

from aws_cdk import (
    core as cdk,
    aws_cloudwatch as cloudwatch,
    aws_ec2 as ec2,
    aws_cloudwatch_actions as cloudwatch_actions,
    aws_sns as sns
)
import boto3

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

from aws_cdk import core

class Ec2CloudwatchAlarmsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _ec2_resource = boto3.resource("ec2", region_name="us-east-1")
        instances = []
        for instance in _ec2_resource.instances.all():
            instances.append(instance.instance_id)

        for instance in instances:
            my_alarm = cloudwatch.Alarm(self, f"CloudWatchAlarm-{instance}",
                                        metric=cloudwatch.Metric(namespace="AWS/EC2",
                                                                 metric_name="CPUUtilization",
                                                                 statistic="avg",
                                                                 period=core.Duration.minutes(
                                                                     5),
                                                                 dimensions_map={
                                                                     "InstanceId": f"{instance}",
                                                                 }
                                                                 ),
                                        threshold=50,
                                        treat_missing_data=cloudwatch.TreatMissingData.BREACHING,
                                        comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
                                        evaluation_periods=1,
                                        )
            my_alarm.add_alarm_action(
                cloudwatch_actions.SnsAction(sns.Topic.from_topic_arn(
                    self, f"MySNSTopic-{instance}", topic_arn="arn:aws:sns:us-east-1:xxxxxxxx:testing"))
            )
