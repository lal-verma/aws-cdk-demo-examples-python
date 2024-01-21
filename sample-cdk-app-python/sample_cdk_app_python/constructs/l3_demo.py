from aws_cdk import (
    aws_lambda as _lambda,
    Stack,
    aws_apigateway as apigateway,
    aws_s3 as s3
)

from constructs import Construct

class L3ConstructsDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        lambdaFunction = _lambda.Function(self, "lambda-l3", 
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("../sample-lambda-functions/"),
            handler="l3_construct.lambda_handler"
            )            

        apigateway.LambdaRestApi(self, 'l3-construct', 
          handler = lambdaFunction,
          proxy = True
        )

    
