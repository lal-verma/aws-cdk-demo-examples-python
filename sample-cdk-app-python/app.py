#!/usr/bin/env python3
import os
import aws_cdk as cdk

app = cdk.App()


from sample_cdk_app_python.tags.tags_demo import (TagsDemoStack_1)
TagsDemoStack_1(app, "TagsDemoStack1")






























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

















