from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    RemovalPolicy,
    App
)
from constructs import Construct
import os

#database tier specific resources/constructs/logic
class DatabaseTier(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamodb.TableV2(self, 'service-db',
                        partition_key=dynamodb.Attribute(
                            name='pk', 
                            type=dynamodb.AttributeType.STRING),
                        removal_policy= RemovalPolicy.DESTROY)
        
        
class ServiceTier(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, lambda_runtime, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _lambda.Function(self, "service-api", 
            function_name='my-fixed-function',
            runtime=lambda_runtime,
            code=_lambda.Code.from_asset("../sample-lambda-functions/"),
            handler="l2_construct.lambda_handler"
            )



#deployment specific logic
class DatabaseTierStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        DatabaseTier(self, 'DatabaseTier', **kwargs)


#deployment specific logic
class ServiceTierStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        DatabaseTier(self, 'DatabaseTier', **kwargs)



app = App()
databasetier_testing = ServiceTierStack(app, 'ServiceTierStack-Test', 
                                         env={
                                             'account': os.getenv('CDK_TESTING_ACCOUNT'), 
                                             'region': os.getenv('CDK_TESTING_REGION')
                                             })
databasetier_production = ServiceTierStack(app, 'ServiceTierStack-Prod', 
                                         env={
                                             'account': os.getenv('CDK_PROD_ACCOUNT'),
                                             'region': os.getenv('CDK_PROD_REGION')
                                             })

