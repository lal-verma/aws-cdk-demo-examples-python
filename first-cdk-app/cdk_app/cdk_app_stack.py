from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)

from constructs import Construct
import aws_cdk.aws_s3 as s3


class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       
        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)