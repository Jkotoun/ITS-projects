Feature: Content management

Scenario: Add method with tool and test case reference
    Given a web browser is at add method form
    When producer fills required method inputs
    And producer adds relation to tool and test case in relations tab
    And producer clicks on save button
    Then producer should see info item created
    And producer should see references to selected tool, method and test case in relations section

Scenario: Delete method
    Given a web browser is at existing method detail page
    When producer clicks on Actions and delete and confirms modal
    Then producer should see info deleted item info
    And producer should not see deleted method in list of methods

Scenario: Create use case:
    Given a web browser is at use case add form
    When producer fills all required inputs
    And producer clicks on save button
    Then producer should see info item created
    And producer should see created use case in use cases list 

Scenario: Create use case requirement:
    Given a web browser is at existing use case detail page
    When producer clicks on add new requirement in navbar
    And producer fills all required inputs 
    And producer clicks on save button
    Then producer should see info item created
    And producer should see requirement detail page
    And producer should see created requirement reference in content section at parent requirement detail page


