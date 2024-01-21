from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
)

from constructs import Construct

# stack for todo database
class TodoDatabaseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #create a dynamodb table
        self.todo_db = dynamodb.Table(self, 'todo-db',
                                    partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING),
                                    removal_policy=RemovalPolicy.DESTROY)
        

# stack for todo service
class TodoServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, todo_db: Construct, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

         #create a lambda function
        todo_service_function = _lambda.Function(self, 'todo-service',
                                                 runtime=_lambda.Runtime.PYTHON_3_9,
                                                 handler='todo_service.handler',
                                                 code=_lambda.Code.from_asset("../sample-lambda-functions/"))
        
        #adding environment variable
        todo_service_function.add_environment('TODO_DB_TABLE_NAME', todo_db.table_name)
        #granting dynamodb read-write permission to lambda
        todo_db.grant_read_write_data(todo_service_function)