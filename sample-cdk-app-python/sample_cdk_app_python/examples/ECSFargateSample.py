from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
)

from constructs import Construct

class EC2SampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #create a VPC
        myVpc = ec2.Vpc(self, "my-VPC", max_azs=1)

        #create an ec2 instance
        myEC2 = ec2.Instance(self, "my-EC2",
                             instance_type=ec2.InstanceType("t2.micro"),
                             machine_image=ec2.AmazonLinuxImage(),
                             vpc=myVpc)

        myanotherEC2 = ec2.Instance(self, "my-another-EC2",
                                    instance_type=ec2.InstanceType("t2.micro"),
                                    machine_image=ec2.AmazonLinuxImage(),
                                    vpc=myVpc)
        
        #create s3 bucket
        myBucket = s3.Bucket(self, "my-s3-bucket")
        myBucket.grant_read_write(myEC2)
        myBucket.grant

        
        





















class ECSFargateSampleStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        #create a VPC
        myVpc = ec2.Vpc(self, "my-VPC")

        #create a security group
        myCluster = ecs.Cluster(self, "my-cluster", vpc=myVpc)

        self.myTaskDefinition = ecs.FargateTaskDefinition(
            self, "my-task-definition", 
            cpu=256,
            memory_limit_mib=512,
            family="my-family",
            execution_role=iam.Role.from_role_arn(
                self,
                "my-role", "arn:aws:iam::XXXXXXXXX:role/ecsTaskExecutionRole"))        
        
        self.myTaskDefinition.add_container("my-container", image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"))
        

