Feature: Debt Scope Assessment

  Background: selecting debt for scope assessment

    Given I am on the public problem page
    When I select debt
    Then I verify I am on the what do you need help with page

  Scenario: Yes I own my own home - no risk - NO MEANS TEST

    When I click option I own my own home
    And I click option NO you are not in risk of losing your home
    Then I verify I am on the legal aid is not usually available for this problem page


  Scenario: Yes I own my own home - at risk - MEANS TEST

    When I click option You own my own home
    And I click option YES you are in risk of losing your home
    Then I verify I am on the about me page


  Scenario: Becoming homeless - MEANS TEST


    When I click option You are homeless
    Then I verify I am on the about me page

  @todo
  Scenario: In rented accommodation - Becoming homeless - MEANS TEST


    When I click option You are living in rented accommodation
    And I click option You are becoming homeless
    Then I verify I am on the about me page

   @todo
  Scenario: In rented accommodation - losing accommodation as UKVI refusing to support - MEANS TEST

    When I click option You are living in rented accommodation
    And I click option You are losing my accommodation because UKVI is refusing support
    Then I verify I am on the about me page

  @todo
  Scenario: In rented accommodation - eviction - eviction with notice - MEANS TEST

    When I click option You are living in rented accommodation
    And I click option Eviction
    And I click option Eviction with notice
    Then I verify I am on the about me page