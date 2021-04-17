Feature: Content management
#test 1
Scenario: Add method with tool, test case and another method reference
    Given a web browser is at add method form
    And at least 1 tool, test case and other method exists
    When producer fills required inputs
    And producer adds relations to existing tool, method nad test case in relations tab
    And producer clicks on save button
    Then producer should see page with added method
    And producer should see info "Item created"
    And producer should see references to selected tool, method and test case in relations section
#test 2
Scenario: Add method with more than 1 reference to tools 
    Given a web browser is at add method form
    And at least 2 tools exist
    When producer fills required inputs 
    And producer adds references to 2 different tools in Relations tab
    And producers clicks on save button
    Then producer should see info "Item created"
    And producer should see both tool references in relations section
#test 3
Scenario: Method reference to tool edit
    Given a web browser is at existing method edit page
    And selected method to edit has at least 1 tool relation 
    When producer removes relation to tool in relations tab 
    And producer clicks on save button
    Then producer should see info "Changes saved"
    And producer should not see removed reference to tool
#test 4
Scenario: Remove of referenced tool updates reference in method
    Given Method referencing some tool exists
    When producer navigates to referenced tool detail page
    And producer deletes tool via actions in navbar
    And producer navigates to method, which was referencing to deleted tool
    Then producer should not see reference to deleted tool in relations section
#test 5
Scenario: Delete method
    Given a web browser is at existing method detail page
    When producer clicks on Actions and delete in navbar
    And producer clicks delete in confirmation modal window
    Then producer should see info deleted item info
    And producer should not see deleted method in list of methods
#test 6
Scenario: Add tool with relation to method and test case
    Given a web browser is at add tool form
    And at least 1 method and test case exists
    When producer fills required inputs
    And producer adds reference to related method and test case
    And producer click on save button
    Then producer should see info item created
    And producer should see reference to method and test case in relations section
#test 7
Scenario: Edit tool
    Given a web browser is at edit existing tool form
    And tool, which is being edited has no related method references
    And at least 1 method exists
    When producer adds reference to some method in relations tab
    And producer clicks on save button
    Then producer should see info changes saved
    And producer should see reference to selected method in relations section
#test 8
Scenario: Delete tool
    Given a web browser is at tool detail page
    When producer clicks on Actions and delete in navbar
    And producer confirm delete in confirmation modal window
    Then producer should see deleted item info
    And producer should not see deleted tool in tools list
#test 9
Scenario: Create use case:
    Given a web browser is at use case add form
    When producer fills all required inputs
    And producer click on save button
    Then producer should see info item created
    And producer should see created use case in use cases list 
#test 10
Scenario: Create use case requirement:
    Given a web browser is at existing use case detail page
    When producer clicks on add new requirement in navbar
    And producer fills all required inputs 
    And producer clicks on save button
    Then producer should see info item created
    And producer should see requirement detail page
    And producer should see created requirement reference in content section at parent requirement detail page
#test 11
Scenario: Create test case
    Given a web browser is at existing requirement detail page
    And at least 1 method exists
    When producer clicks on add new test case in navbar 
    And producer fills all required inputs
    And producer adds reference to existing method in test case
    And producers clicks on save button
    Then producer should see info item created
    And producer should see reference to selected method in test case method section at test case page
    And producer should see reference to test case in content section at parent requirement page
#test 12
Scenario: Create evaluation scenario:
    Given a web browser is at existing use case detail page
    And displayed use case has at least 1 requirement
    When producer clicks on add evaluation scenario in navbar
    And producer fills required inputs
    And adds reference to existing requirement in Evaluation scenario requirements tab
    And producer clicks on save button
    Then producer should see info item created
    And producer should see evaluation scenario detail page
    And producer should see reference to selected requirement in evaluation scenario requirements list
    And producer should see reference to created evaluation scenario at parent use case detail page
#test 13
Scenario: Add evaluation scenario reference to use case
    Given a web browser is at existing use case detail page
    And evaluation scenario exists
    When producer clicks edit in navbar
    And producer adds reference to existing evaluation scenario in Use case evaluation scenarios tab
    And producers clicks on save button
    Then producer should see info changes saved
    And producer should see reference to evaluation scenario in evaluation scenarios list
#test 14
Scenario: Add test case reference to requirement
    Given a web browser is at existing requirement detail page
    And at least 1 test case exists
    When producer clicks on edit in navbar
    And producer adds reference to some test case in requirement test cases tab
    And producer clicks on save button
    Then producer should see info changes saved
    And producer should see reference to selected test case in requirement test cases section







