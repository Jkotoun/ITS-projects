Feature: Content visibility

Scenario: Set public method as private
    Given a browser is at public method detail page
    When producer changes state to private
    Then producer should see info item state changed
    And producer should see published method detail page
    But consumer should not see this method in methods list

Scenario: Set private method as public
    Given a browser is at private method detail page
    When producer changes state to public
    Then producer should see info item state changed
    And producer should see published method detail page
    And consumer should see this method in methods list
