
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from steps.classes import ploneGlobal
def before_all(context):
    try:
        context.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        context.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
    context.driver.implicitly_wait(5)
    context.base_url = "http://localhost:8080/VALU3S"
    
    
def after_all(context):
    context.driver.quit()

def before_scenario(context, scenario):
    ploneGlobal.login(context.driver, "itsadmin", "itsadmin", context.base_url)