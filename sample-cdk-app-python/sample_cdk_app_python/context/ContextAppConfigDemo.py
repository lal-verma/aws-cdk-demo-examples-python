from aws_cdk import (
  Stack,
  aws_ec2 as ec2,
  aws_autoscaling as autoscaling,
  aws_ecs as ecs,
)
from constructs import Construct


class ContextAppConfigDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # existing vpc
        myExistingVpc = ec2.Vpc.from_lookup(self, "demo-cache-vpc",
                                            vpc_id=self.node.try_get_context('vpc_id'))


        # creating a new EC2 Auto Scaling Group
        asg = autoscaling.AutoScalingGroup(self, "demo-cache-asg",
                                            vpc=myExistingVpc,
                                            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2,
                                                                              ec2.InstanceSize.MICRO),
                                            machine_image=ecs.EcsOptimizedImage.amazon_linux2(),
                                            min_capacity=0,
                                            max_capacity=10,
                                            )                                      