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