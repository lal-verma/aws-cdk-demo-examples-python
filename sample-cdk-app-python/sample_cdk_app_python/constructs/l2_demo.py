from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    Stack,
    aws_iam as iam,
)

from constructs import Construct

class L2ConstructsDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        lambdaFunction = _lambda.Function(self, "lambda-l2", 
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("../sample-lambda-functions/"),
            handler="l2_construct.lambda_handler"
            )