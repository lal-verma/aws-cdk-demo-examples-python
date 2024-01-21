from aws_cdk import (
    Stack,
    NestedStack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class ServiceTierStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _lambda.Function(self, "service-api", 
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("../sample-lambda-functions/"),
            handler="l2_construct.lambda_handler"
            )
        

class DatabaseTierStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamodb.TableV2(self, 'service-db',
                        partition_key=dynamodb.Attribute(name='pk', type=dynamodb.AttributeType.STRING))
    
                      
        
class MyApplication(Stack):

    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        ServiceTierStack(self, 'BusinessTierStack')
        DatabaseTierStack(self, 'DatabaseTierStack')