from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    Tags
)

from constructs import Construct

class TagsExcludeDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
    

        todoservice_function = _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),)
           

        Tags.of(todoservice_function).add("microservice", "todo-service", 
                          exclude_resource_types=["AWS::IAM::Role"]);    


class TagsIncludeDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
    

        todoservice_function = _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),)
           

        Tags.of(todoservice_function).add("microservice","todo-service", 
                          include_resource_types=["AWS::Lambda::Function"]);    