from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from classes import *
import time
@given('a web browser is at add method form')
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods/++add++method")

@when('producer fills required method inputs')
def step_impl(context):
    form = addForm(context.driver)
    form.method_fill_required("method1_name_test_","purpose","desc","strength 100", "limitations 0")

@when('producer adds relation to tool and test case in relations tab')
def step_impl(context):
    form = addForm(context.driver)
    form.addToolRelation("testos")
    form.addTestcaseRelation("UC1_TC_1")
    
@when('producer clicks on save button')
def step_impl(context):
    form = addForm(context.driver)
    form.save()

@then('producer should see info item created')
def step_impl(context):
    assert ploneGlobal.message_displayed(context.driver, "Info Item created")

@then('producer should see references to selected tool, method and test case in relations section')
def step_impl(context):
    detail = detailPage(context.driver)
    assert detail.testcase_reference_exists() and detail.tool_reference_exists()

@given('a web browser is at existing method detail page')
def step_impl(context):
    context.driver.get(f"{context.base_url}/methods")
    context.driver.find_element_by_xpath("//*[@id='content-core']//a[text()='method1_name_test_']").click()

@when('producer clicks on Actions and delete and confirms modal')
def step_impl(context):
    ploneGlobal.delete(context.driver)

@then('producer should see info deleted item info')
def step_impl(context):
    assert ploneGlobal.message_displayed(context.driver, "Info method1_name_test_ has been deleted.")

@then('producer should not see deleted method in list of methods')
def step_impl(context):
    methods = detailsList(context.driver, f"{context.base_url}/methods")
    assert not methods.detail_name_displayed("method1_name_test_")


@given('a web browser is at use case add form')
def step_impl(context):
    context.driver.get(f"{context.base_url}/use-cases/++add++use_case")

@when('producer fills all required inputs')
def step_impl(context):
    form = addForm(context.driver)
    form.usecase_fill_required("usecase_title_test_1", "usecase description")

@then('producer should see created use case in use cases list')
def step_impl(context):
    usecases = detailsList(context.driver, f"{context.base_url}/use-cases")
    usecases.detail_name_displayed("usecase_title_test_1")

@given('a web browser is at existing use case detail page')
def step_impl(context):
    usecases = detailsList(context.driver, f"{context.base_url}/use-cases")
    usecases.get_any_item().click()
@when('producer clicks on add new requirement in navbar')
def step_impl(context):
    context.find_element_by_xpath("//*[@id='plone-contentmenu-factories']/a").click()
    context.find_element_by_id("requirement").click()
@when('producer fills all required requirement inputs')
def step_impl(context):
    requirements_form = addForm(context.driver)
    requirements_form.requirement_fill_required("requirement_test_1")
    