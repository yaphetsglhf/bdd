from behave import *


@given('假如')
def step_impl(context):
    pass


@when('当')
def step_impl(context):
    assert True is not False


@then('那么')
def step_impl(context):
    assert True is not False
