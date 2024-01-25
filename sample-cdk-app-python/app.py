#!/usr/bin/env python3
import os
import aws_cdk as cdk

app = cdk.App()

from sample_cdk_app_python.tags.tags_priority_demo import TagsPriorityDemoStack
TagsPriorityDemoStack(app, "TagsPriorityDemoStack")























#uncomment the following block to enable Resource removal demo
""" from sample_cdk_app_python.resources.removal_policy_demo import (RemovalPolicyDemoStack)
RemovalPolicyDemoStack(app, "RemovalPolicyDemoStack")
 """

#uncomment the following block to enable Resource Referece Different Stack Demo
""" 
from sample_cdk_app_python.resources.rr_different_stack_demo import (TodoDatabaseStack, TodoServiceStack)
todo_db_stack = TodoDatabaseStack(app, "TodoDatabaseStack")
todo_service_stack = TodoServiceStack(app, "TodoServiceStack", todo_db_stack.todo_db)
 """


#uncomment the following block to enable ContextAppConfigDemoStack
""" app_config = app.node.try_get_context('app-config')
ContextAppConfigDemoStack(app, "ContextAppConfigDemoStack", 
                      env=cdk.Environment(
                          account=app_config['account'], 
                          region=app_config['region']))
 """

#uncomment the following block to enable ContextCacheDemoStack
""" from sample_cdk_app_python.context.ContextCacheDemo import (ContextCacheDemoStack)
ContextCacheDemoStack(app, "ContextCacheDemoStack", 
                      env=cdk.Environment(
                          account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                          region=os.getenv('CDK_DEFAULT_REGION')))


 """

app.synth()

















