Feature: Content visibility

#test 15
Scenario: Set public method as private
    Given a browser is at public method detail page
    When producer changes state to private
    Then producer should see info item state changed
    And producer should see method detail page
    But consumer should not see this method in methods list
#test 16
Scenario: Set private tool as public
    Given private tool exists
    And a browser is at private tool detail page
    When producer changes state to public
    Then producer should see info item state changed
    And producer should see tool detail page
    And consumer should see tool in list of tools
#test 17
Scenario: Create tool with publish time in future:
    Given a browser is at add tool form
    When producer fills required inputs
    And producer fills tomorow date in publishing date
    And producer clicks on save button
    And producer sets state to public
    And producer should see created tool detail page
    But consumer should not see tool in tools list
#test 18
Scenario: Create tool with publish time in past:
    Given a browser is at add tool form
    When producer fills required inputs
    And producer fills yesterday date in publishing date
    And producer clicks on save button
    And producer sets state to public
    Then producer should see created tool detail page
    And consumer should see tool in tools list
#test 19
Scenario: Add use case default state is private
    Given a browser is at add use case form
    When producer fills required inputs
    And producer clicks on save button
    Then producer should see created use case in use cases list
    But consumer should not see use case in use cases list 
