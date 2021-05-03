from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 

from pages import *


@given('a browser is at public method detail page')
def step_impl(context):
    context.driver.get(context.base_url)
    ploneGlobal.login(context.driver, "itsadmin", "itsadmin", context.base_url)
    methodList = detailsList(context.driver, f"{context.base_url}/methods")
    methodList.load()
    public_method= methodList.get_item_with_state("published")
    global selectedMethod
    selectedMethod = public_method.text
    context.driver.get(public_method.get_attribute("href"))
    

@when('producer changes state to private')
def step_impl(context):
    ploneGlobal.set_private(context.driver)

@then('producer should see info item state changed')
def stem_impl(context):
    assert ploneGlobal.message_displayed(context.driver, "Info Item state changed." )

@then ('producer should see published method detail page')
def stem_impl(context):
    detail = detailPage(context.driver)
    assert detail.get_title() != ""

@then ('consumer should not see this method in methods list')      
def stem_impl(context):
    ploneGlobal.logout(context.driver)
    methodsListPage = detailsList(context.driver, f"{context.base_url}/methods")
    methodsListPage.load()
    assert not methodsListPage.detail_name_displayed(selectedMethod)
    ploneGlobal.login(context.driver, "itsadmin", "itsadmin", context.base_url)

@given('a browser is at private method detail page')
def step_impl(context):
    context.driver.get(context.base_url)
    methodList = detailsList(context.driver, f"{context.base_url}/methods")
    methodList.load()
    public_method= methodList.get_item_with_state("private")
    global selectedMethod
    selectedMethod = public_method.text
    context.driver.get(public_method.get_attribute("href"))

@when('producer changes state to public')
def step_impl(context):
    ploneGlobal.set_public(context.driver)

@then ('consumer should see this method in methods list')      
def step_impl(context):
    ploneGlobal.logout(context.driver)
    methodsListPage = detailsList(context.driver, f"{context.base_url}/methods")
    methodsListPage.load()
    assert methodsListPage.detail_name_displayed(selectedMethod)
    ploneGlobal.login(context.driver, "itsadmin", "itsadmin", context.base_url)

