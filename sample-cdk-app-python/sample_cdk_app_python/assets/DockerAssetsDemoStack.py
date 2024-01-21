from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ecr_assets as ecr_assets,
)

from constructs import Construct


class DockerAssetsDemoStack(Stack): 
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)

        task_definition = ecs.FargateTaskDefinition(self, "todo-app-task", 
                                                    memory_limit_mib=1024,cpu=512)

        
        ecr_assets.DockerImageAsset(self, 'todo-container-image',
                                    directory='../sample-container-app',
                                    asset_name='todo-app-container-image')
    
        task_definition.add_container('todo-app-container', 
                                    image=ecs.ContainerImage.from_docker_image_asset(docker_asset),
                                    )
