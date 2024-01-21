from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    aws_s3 as s3,
)
from constructs import Construct



class PolicyDemoTraditional(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)


        todo_db = dynamodb.Table(self, 'todo-db', 
                        partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING),
                        removal_policy= RemovalPolicy.DESTROY)
          
        todoservice_function = _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),)
           
        todoservice_function.add_to_role_policy(iam.PolicyStatement(
            actions=['dynamodb:*'],
            resources=[todo_db.table_arn],
            effect=iam.Effect.ALLOW
        ))

        

        todoservice_function.add_environment('TODO_DB_TABLE_NAME', todo_db.table_name)

        iam.Role.fr


class PolicyDemoGrant(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)


        todo_db = dynamodb.Table(self, 'todo-db', 
                        partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING),
                        removal_policy= RemovalPolicy.DESTROY)
          
        todoservice_function = _lambda.Function(self, 'todo-service', 
                        runtime=_lambda.Runtime.PYTHON_3_9,
                        handler='todo_service.handler',
                        code=_lambda.Code.from_asset("../sample-lambda-functions/"),)
           
        todoservice_function.add_environment('TODO_DB_TABLE_NAME', todo_db.table_name)

        #grant reference
        todo_db_grant = todo_db.grant_read_write_data(todoservice_function)


class RoleDefinitionDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        lambda_role = iam.Role(self, 'lambda-role', 
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),   
        )

        lambda_role.add_to_policy(iam.PolicyStatement(
            actions=['dynamodb:*'],
            resources=['*'],
            effect=iam.Effect.ALLOW
        ))

        _lambda.Function(self, 'todo-service', 
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler='todo_service.handler',
            code=_lambda.Code.from_asset("../sample-lambda-functions/"),
            role=lambda_role)


class DefaultRoleDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        todo_db = dynamodb.Table(self, 'todo-db', 
                        partition_key=dynamodb.Attribute(
                            name='id', type=dynamodb.AttributeType.STRING),
                        removal_policy= RemovalPolicy.DESTROY)

        todo_service_function  = _lambda.Function(self, 'todo-service', 
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler='todo_service.handler',
            code=_lambda.Code.from_asset("../sample-lambda-functions/"))
        
        todo_service_function.add_to_role_policy(iam.PolicyStatement(
            actions=['dynamodb:*'],
            resources=[todo_db.table_arn],
            effect=iam.Effect.ALLOW
        ))



class ResourcePolicyDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        demo_bucket = s3.Bucket(self, 'XXXXXXXXXXX')

        lambda_role = iam.Role(self, 'lambda-role', 
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),   
        )

        demo_bucket.add_to_resource_policy(iam.PolicyStatement(
            actions=['s3:*'],
            resources=[demo_bucket.bucket_arn],
            principals=[lambda_role],
        ))

