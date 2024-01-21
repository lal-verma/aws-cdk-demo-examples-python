from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    Stack,
    aws_iam as iam,
)

from constructs import Construct

class L1ConstructsDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        lambdaRole = iam.Role(self, "l1-lambda-role",
                                    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                                    managed_policies=[
                                        iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
                                    ]
                                    )                                              

        lambdaFunction = _lambda.CfnFunction(self, "lambda-l1", 
            runtime="python3.9",
            code=_lambda.CfnFunction.CodeProperty(
                s3_bucket="sample-code-2347985456",
                s3_key="python/l1_construct.zip"                
            ),    
            handler="l1_construct.lambda_handler",
            role=lambdaRole.role_arn,
            )