from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    Tags
)

from constructs import Construct

class TagsDemoStack_1(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
    
        dynamodb.Table(self, 'todo-db', 
                       partition_key=dynamodb.Attribute(name='id', 
                                                        type=dynamodb.AttributeType.STRING),
                       removal_policy=RemovalPolicy.DESTROY,)

        _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),)
           
        


class TagsDemoStack_2(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
    
        dynamodb.Table(self, 'todo-db', 
                       partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING),
                       removal_policy=RemovalPolicy.DESTROY,)

        todo_service_function = _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),)
           
        Tags.of(todo_service_function).add('microservice', 'todo-service-v2')
