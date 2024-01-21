from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
)

from constructs import Construct

class RemovalPolicyDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        #create an s3 bucket
        s3.Bucket(self, 'my-bucket-removal-policy', 
                  removal_policy=RemovalPolicy.DESTROY,
                  auto_delete_objects=True)

        #create a dynamodb table
        dynamodb.Table(self, 'my-table-removal-policy', 
                       partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING),
                       removal_policy=RemovalPolicy.DESTROY,)
