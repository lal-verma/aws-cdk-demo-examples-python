from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    RemovalPolicy,
    IAspect,
    App,
    aws_s3 as s3,
    aws_ecs as ecs,
    aws_ecr_assets as ecr_assets,
)
from constructs import Construct
import os
import jsii

#do not change the logical id
class DatabaseTier(Construct):

    def __init__(self, scope: Construct, 
                 construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamodb.TableV2(self, 'service-db',
                        partition_key=dynamodb.Attribute(
                            name='pk', 
                            type=dynamodb.AttributeType.STRING),
                        removal_policy= RemovalPolicy.DESTROY)
        




class DatabaseTierStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        DatabaseTier(self, 'DatabaseTier')


@jsii.implements(IAspect)
class LogicalIdAspect: 
    def visit(self, node):
        if isinstance(node, dynamodb.TableV2):
            node.node.override_logical_id("my-fixed-logical-id")


# build assets once 
class DockerAssetsDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        task_definition = ecs.FargateTaskDefinition(self, "todo-app-task", 
                                                    memory_limit_mib=1024,cpu=512)

        docker_asset = ecr_assets.DockerImageAsset(self, 'todo-container-image',
                                                    directory='../sample-container-app',
                                                    asset_name='todo-app-container-image')
    
        task_definition.add_container('todo-app-container', 
                                    image=ecs.ContainerImage.from_docker_image_asset(docker_asset),
                                    )
        


app = App()
DockerAssetsDemoStack(app, "DockerAssetsDemoStack-Test", 
                      env={'region': 'us-east-1'}, 
                      
                      )
DockerAssetsDemoStack(app, "DockerAssetsDemoStack-Prod",)







app = App()
dts_test = DatabaseTierStack(app, "DatabaseTierStack-Test",
                      env={'account': os.getenv('CDK_TESTING_ACCOUNT'), 'region': os.getenv('CDK_TESTING_REGION')},
                      termination_protection=False,
                      analytics_reporting=False)

dts_stage = DatabaseTierStack(app, "DatabaseTierStack-Stage",
                      env={'account': os.getenv('CDK_STAGE_ACCOUNT'), 'region': os.getenv('CDK_STAGE_REGION')},
                      termination_protection=False,
                      analytics_reporting=True)

dts_prod = DatabaseTierStack(app, "DatabaseTierStack-Prod",
                      env={'account': os.getenv('CDK_PROD_ACCOUNT'), 'region': os.getenv('CDK_PROD_REGION')},
                      termination_protection=True,
                      analytics_reporting=True)









