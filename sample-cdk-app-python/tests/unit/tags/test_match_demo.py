import aws_cdk as core
from aws_cdk.assertions import Match,Template

from sample_cdk_app_python.tags.tags_demo import (TagsDemoStack_1)
import pytest

@pytest.fixture
def init_template():
    app = core.App()
    stack = TagsDemoStack_1(app, "tags-demo")
    template = Template.from_stack(stack)
    return template

def test_function_runtime(init_template):

    init_template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.9"
    })

def test_function_tags(init_template):
    init_template.has_resource_properties("AWS::Lambda::Function", {
        "Tags": Match.array_equals([{"Key":"microservice", "Value":Match.any_value()}])
    })
