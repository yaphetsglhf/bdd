from behave import *


@given('I put {thing} in a blender')
def step_impl(context, thing):
    print(thing)
    pass


@when('I switch the blender on')
def step_impl(context):
    assert True is not False


@then('it should transform into {otherthing}')
def step_impl(context, otherthing):
    print(otherthing)
    assert context.failed is False
