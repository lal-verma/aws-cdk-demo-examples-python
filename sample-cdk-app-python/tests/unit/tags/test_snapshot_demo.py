import aws_cdk as core
import aws_cdk.assertions as assertions

from sample_cdk_app_python.tags.tags_demo import (TagsDemoStack_1)


def test_function_snapshot(snapshot):
    app = core.App()
    stack = TagsDemoStack_1(app, "tags-demo")
    template = assertions.Template.from_stack(stack)

    assert template.to_json() == snapshot
                                    