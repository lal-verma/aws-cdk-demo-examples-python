from aws_cdk import (
    aws_s3 as s3,
    Stack,
    RemovalPolicy
)

from constructs import Construct

class ConstructIDDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        # create a new S3 bucket
        myFirstbucket = s3.Bucket(self, "my-first-bucket", 
                                  bucket_name="my-first-bucket-abcdefghijklmnopqrstuvwxyz",
                                  versioned=False,
                                  encryption=s3.BucketEncryption.KMS_MANAGED,
                                  object_lock_enabled=True,
                                  removal_policy=RemovalPolicy.DESTROY,
                                  auto_delete_objects=True)

        # create another s3 bucket
        mySecondBucket = s3.Bucket(self, "my-second-bucket", 
                                   removal_policy=RemovalPolicy.DESTROY,
                                   auto_delete_objects=True)
