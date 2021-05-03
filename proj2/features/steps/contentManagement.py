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
    usecases.load()
    assert usecases.detail_name_displayed("usecase_title_test_1")

@given('a web browser is at existing use case detail page')
def step_impl(context):
    usecases = detailsList(context.driver, f"{context.base_url}/use-cases")
    usecases.load()
    usecases.get_any_item().click()
@when('producer clicks on add new requirement in navbar')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='plone-contentmenu-factories']/a").click()
    context.driver.find_element_by_id("requirement").click()
@when('producer fills all required requirement inputs')
def step_impl(context):
    requirements_form = addForm(context.driver)
    requirements_form.requirement_fill_required("requirement_test_1")
@then('producer should see item detail page')
def step_impl(context):
    detail = detailPage(context.driver)
    assert detail.get_title() != ""
@then('producer should see created requirement reference in content section at parent use case detail page')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='breadcrumbs-2']/a").click()
    content = detailsList(context.driver,context.driver.current_url)
    assert content.detail_name_displayed("requirement_test_1")

@given('a web browser is at existing requirement detail page')
def step_impl(context):
    context.driver.find_element_by_link_text("requirement_test_1").click()

@when('producer clicks on add new test case in navbar')
def step_impl(context):
    ploneGlobal.add_testcase_action(context.driver)

@when('producer fills all required testcase inputs')
def step_impl(context):
    testcase_form = addForm(context.driver)
    testcase_form.testcase_fill_required("test_case_test_1", "tc_1_tst_id")

@when('producer adds reference to existing method in test case')
def stepimpl(context):
    testcase_form = addForm(context.driver)
    testcase_form.add_method_reference_in_testcase("test_case_test_1")

@then('producer should see reference to selected method in test case method section at test case page')
def stepimpl(context):
    assert context.driver.find_element_by_xpath("//*[@id='form-widgets-test_case_v_v_method']//a").is_displayed()

@then('producer should see reference to test case in content section at parent requirement page')
def stepimpl(context):
    context.driver.find_element_by_xpath("//*[@id='breadcrumbs-3']/a").click()
    content = detailsList(context.driver,context.driver.current_url)
    assert content.detail_name_displayed("test_case_test_1")
@when('producer clicks on add evaluation scenario in navbar')
def step_impl(context):
    ploneGlobal.add_evaluation_scenario(context.driver)

@when('producer fills required evaluation scenario inputs')
def step_impl(context):
    scenario_form = addForm(context.driver)
    scenario_form.evaluation_scenario_fill_required("evaluation_scenario_test_1", "es_tst_1", "description test")

@when('producer adds reference to existing requirement in Evaluation scenario requirements tab')
def step_impl(context):
    scenario_form = addForm(context.driver)
    scenario_form.add_scenario_requirement_reference("requirement_test_1")

@then('producer should see reference to selected requirement in evaluation scenario requirements list')
def step_impl(context):
    assert context.driver.find_element_by_xpath("//*[@id='form-widgets-evaluation_scenario_requirements_list']//span[text()='requirement_test_1']").is_displayed()
@then('producer should see reference to created evaluation scenario at parent use case detail page')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='breadcrumbs-2']/a").click()
    assert context.driver.find_element_by_xpath("//a[text()='requirement_test_1']").is_displayed()