from behave import given, when, then
from pages.home_page.home_executors import HomePage


@given("I am on the home page")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open("https://the-internet.herokuapp.com")

@then("I should see the title as '{expected_title}'")
def step_impl(context, expected_title):
    actual_title = context.home_page.get_header()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

@when("I perform some action")
def step_impl(context):
    pass
    # Implement the action