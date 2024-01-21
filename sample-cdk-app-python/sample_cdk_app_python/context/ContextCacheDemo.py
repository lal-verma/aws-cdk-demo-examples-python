from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling
)
from constructs import Construct


class ContextCacheDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        myExistingVpc = ec2.Vpc.from_lookup(self, 'context-cache-vpc',
                                            vpc_id="vpc-4c244827")


        autoscaling.AutoScalingGroup(self, 'context-cache-asg',
                                     vpc=myExistingVpc,
                                     instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.MICRO),
                                     machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                     min_capacity=1,
                                     max_capacity=11,
                                     )