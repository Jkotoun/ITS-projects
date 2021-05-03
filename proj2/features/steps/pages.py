from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import time
import uuid
class detailsList:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
    def load(self):
        self.driver.get(self.url)
    def detail_name_displayed(self, name):
        try:
            self.driver.find_element_by_xpath(f"//*[@id='content-core']//span[@class='summary']/a[text()='{name}']")
        except NoSuchElementException:
            return False
        return True
    def get_item_with_state(self, state):
        return self.driver.find_element_by_xpath(f"//*[@id='content-core']//span[@class='summary']/a[contains(@class, 'state-{state}')]")
    def get_any_item(self):
        return self.driver.find_element_by_xpath(f"//*[@id='content-core']//span[@class='summary']/a")
        

class detailPage:
    def __init__(self, driver):
        self.driver = driver
    def get_title(self):
        return self.driver.find_element_by_xpath("//*[@id='content']//h1").text
    def tool_reference_exists(self):
        return self.driver.find_element_by_xpath("//*[@id='formfield-form-widgets-tools']//a").text != ""
    def testcase_reference_exists(self):
        return self.driver.find_element_by_xpath("//*[@id='formfield-form-widgets-tools']//a").text != ""
    
    

class ploneGlobal:
    def __init__(self, driver):
        self.driver = driver
    @staticmethod
    def set_private(driver):
        driver.find_element_by_xpath("//*[@id='plone-contentmenu-workflow']/a").click()
        driver.find_element_by_xpath("//*[@id='workflow-transition-reject']").click()
    @staticmethod
    def set_public(driver):
        driver.find_element_by_xpath("//*[@id='plone-contentmenu-workflow']/a").click()
        driver.find_element_by_xpath("//*[@id='workflow-transition-publish']").click()
    @staticmethod
    def delete(driver):
        driver.find_element_by_id("plone-contentmenu-actions").click()
        driver.find_element_by_id("plone-contentmenu-actions-delete").click()
        driver.find_element_by_xpath("//*[@class='pattern-modal-buttons']/input[@value='Delete']").click()
    @staticmethod
    def message_displayed(driver ,text):
        return driver.find_element_by_xpath("//*[@id='global_statusmessage']/div").text == text
    @staticmethod
    def login(driver, name, password, base_url):
        driver.get(f"{base_url}/login")
        driver.find_element_by_id("__ac_name").send_keys(name)
        driver.find_element_by_id("__ac_password").send_keys(password)
        driver.find_element_by_xpath("//*[@id='buttons-login']").click()
    @staticmethod
    def logout(driver):
        driver.find_element_by_xpath("//*[@id='portal-personaltools']//a").click()
        driver.find_element_by_xpath("//*[@id='personaltools-logout']").click()
    @staticmethod
    def add_testcase_action(driver):
        driver.find_element_by_id("plone-contentmenu-factories").click()
        driver.find_element_by_id("test_case").click()
    @staticmethod
    def add_evaluation_scenario(driver):
        driver.find_element_by_id("plone-contentmenu-factories").click()
        driver.find_element_by_id("evaluation_scenario").click()

class addForm:
    def __init__(self, driver):
        self.driver = driver
    def method_fill_required(self, name, purpose, description, strength, limitations):
        self.driver.find_element_by_id("form-widgets-IBasic-title").send_keys(name)
        self.driver.find_element_by_id("form-widgets-method_purpose").send_keys(purpose)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_id("tinymce").send_keys(description)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_id("tinymce").send_keys(strength)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element_by_id("tinymce").send_keys(limitations)
        self.driver.switch_to.default_content()
    def usecase_fill_required(self, title, description):
        self.driver.find_element_by_id("form-widgets-IBasic-title").send_keys(title)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_id("tinymce").send_keys(description)
        self.driver.switch_to.default_content()
    def requirement_fill_required(self, title):
        self.driver.find_element_by_id("form-widgets-IDublinCore-title").send_keys(title)
    def evaluation_scenario_fill_required(self, title, id, description):
        self.driver.find_element_by_id("form-widgets-IBasic-title").send_keys(title)
        self.driver.find_element_by_id("form-widgets-evaluation_secnario_id").send_keys(id)
        self.driver.find_element_by_id("form-widgets-evaluation_scenario_textual_description").send_keys(description)
    def addToolRelation(self, tool_name):
        self.driver.find_element_by_id("autotoc-item-autotoc-2").click()
        self.driver.find_element_by_xpath("//*[@id='formfield-form-widgets-tools']//a[@class='crumb']").click()
        self.driver.find_element_by_id("s2id_autogen12").send_keys(tool_name)
        self.driver.find_element_by_xpath("//*[@id='select2-drop']//a[@class='pattern-relateditems-result-select selectable']").click()
    def testcase_fill_required(self, title, id):
        self.driver.find_element_by_id("form-widgets-IBasic-title").send_keys(title)
        self.driver.find_element_by_id("form-widgets-test_case_id").send_keys(id)
    def addTestcaseRelation(self, testcase_name):
        self.driver.find_element_by_id("autotoc-item-autotoc-2").click()
        self.driver.find_element_by_xpath("//*[@id='formfield-form-widgets-test_case_or_verification_and_validation_activity']//a[@class='crumb']").click()
        self.driver.find_element_by_id("s2id_autogen8").send_keys(testcase_name)
        self.driver.find_element_by_xpath("//*[@id='select2-drop']//a[@class='pattern-relateditems-result-select selectable']").click()
    def save(self):
        self.driver.find_element_by_id("form-buttons-save").click()
    def add_method_reference_in_testcase(self, testcase_name):
        self.driver.find_element_by_xpath("//*[@class='crumb']").click()
        self.driver.find_element_by_id("s2id_autogen2").send_keys("Combinatorial Testing")
        self.driver.find_element_by_xpath("//*[@id='select2-drop']//a[@class='pattern-relateditems-result-select selectable']").click()
    def add_scenario_requirement_reference(self, requirement_name):
        self.driver.find_element_by_id("autotoc-item-autotoc-1").click()
        self.driver.find_element_by_xpath("//*[@id='formfield-form-widgets-evaluation_scenario_requirements_list']//a").click()
        self.driver.find_element_by_id("s2id_autogen2").send_keys(requirement_name)
        self.driver.find_element_by_xpath("//*[@id='select2-drop']//a[@class='pattern-relateditems-result-select selectable']").click()


