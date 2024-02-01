from aws_cdk import(
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)

from constructs import Construct

#database tier construct

class DatabaseTier(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        #create dyanamodb table
        self.todo_db = dynamodb.Table(self, "TodoDB",
                                partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
        )

#service tier construct

class ServiceTier(Construct):
    def __init__(self, scope: Construct, id: str, todo_db_table: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        #create lambda function
        self.todo_service = _lambda.Function(self, "TodoService",
                                        runtime=_lambda.Runtime.PYTHON_3_9,
                                        handler="todo_service.handler",
                                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),
                                        environment={
                                            "TODO_DB_TABLE_NAME": todo_db_table
                                        }
        )


class TodoApplicationStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        #create database tier construct
        database_tier = DatabaseTier(self, "DatabaseTier")

        #create service tier construct
        service_tier = ServiceTier(self, "ServiceTier", todo_db_table=database_tier.todo_db.table_name)

        #create apis through api gateway
        apigateway.LambdaRestApi(self, "TodoApi",
                                 handler=service_tier.todo_service,
                                 proxy=True,
        )

        database_tier.todo_db.grant_read_write_data(service_tier.todo_service)

    
