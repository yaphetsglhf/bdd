from behave import *
import requests


@given('请求接口')
def step_impl(context):
    resp = requests.get('https://bff.bookoom.com/graphql')
    context.resp = resp
    assert resp.status_code == 401


@when('没有token')
def step_impl(context):
    print(context.resp)
    assert True is not False


@then('401')
def step_impl(context):
    print(context)
