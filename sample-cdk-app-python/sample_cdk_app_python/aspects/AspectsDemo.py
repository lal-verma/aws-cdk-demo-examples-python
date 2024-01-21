import jsii

from aws_cdk import (
    Aspects,Tags,Stack,RemovalPolicy, IAspect, Annotations,
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
   )

from constructs import Construct
    
class AspectsDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        #defining sample s3 buckets
        s3.Bucket(self, 'test-bucket-1', 
            versioned= True,
            auto_delete_objects=True,
            removal_policy=RemovalPolicy.DESTROY)
        
        s3.Bucket(self, 'test-bucket-2', 
            auto_delete_objects=True,
            removal_policy=RemovalPolicy.DESTROY)

        s3.Bucket(self, 'test-bucket-3', 
            versioned=False,
            auto_delete_objects=True,
            removal_policy=RemovalPolicy.DESTROY)
        
        dynamodb.TableV2(self, 'test-table-1',
                         partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING) 
                         )

        dynamodb.Table(self, 'test-table-2',
                         partition_key=dynamodb.Attribute(name='id', type=dynamodb.AttributeType.STRING) 
                         )
        
        Aspects.of(self).add(BucketVersioningAspect())
        Aspects.of(self).add(DynamodbAspect())




@jsii.implements(IAspect)
class BucketVersioningAspect: 
    def visit(self, node):
        if isinstance(node, s3.CfnBucket):
            if not node.versioning_configuration or node.versioning_configuration.status != 'Enabled':
                Annotations.of(node).add_error('Bucket versioning is not enabled')


@jsii.implements(IAspect)
class DynamodbAspect: 
    def visit(self, node):
        if isinstance(node, dynamodb.CfnTable):
            Annotations.of(node).add_error('Only global tables are allowed')
    









""" @jsii.implements(IAspect)
class BucketEncryptionAspect:     
    def visit(self, node):
        if isinstance(node, s3.CfnBucket):
            if not node.bucket_encryption:
                Annotations.of(node).add_error("Bucket encryption is required")
        else:
            return
        
 """