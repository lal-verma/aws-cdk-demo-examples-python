from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)

from constructs import Construct

class S3AssetsDemoStack(Stack):  
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
    
        todoservice_function = _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/")) 