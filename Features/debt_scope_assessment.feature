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


  Scenario: In rented accommodation - Becoming homeless - MEANS TEST


    When I click option You are living in rented accommodation
    And I click option You are becoming homeless
    Then I verify I am on the about me page


  Scenario: In rented accommodation - losing accommodation as UKVI refusing to support - MEANS TEST

    When I click option You are living in rented accommodation
    And I click option You are losing my accommodation because UKVI is refusing support
    Then I verify I am on the about me page


  Scenario: In rented accommodation - eviction - eviction with notice - MEANS TEST

    When I click option You are living in rented accommodation
    And I click option Eviction
    And I click option Eviction with notice
    Then I verify I am on the about me page


  Scenario: In rented accommodation - eviction - unlawful eviction - MEANS TEST

    When I click option You are living in rented accommodation
    And I click option Eviction
    And I click option Unlawful eviction
    Then I verify I am on the about me page


  Scenario: In rented accommodation - home in disrepair - risk of injury/illness - MEANS TEST


    When I click option You are living in rented accommodation
    And I click option Your home is in disrepair
    And I click option YES this puts you in risk of injury or illness
    Then I verify I am on the about me page


  Scenario: In rented accommodation - home in disrepair - no risk of injury/illness - NO MEANS TEST


    When I click option You are living in rented accommodation
    And I click option Your home is in disrepair
    And I click option NO you are not in risk of injury or illness
    Then I verify I am on the legal aid is not usually available for this problem page


  Scenario: In rented accommodation - harrasment - a neighbour or landlord - MEANS TEST


    When I click option You are living in rented accommodation
    And I click option Harassment
    And I click option By a neighbour or landlord
    Then I verify I am on the about me page


  Scenario: In rented accommodation - harrasment - a partner or family member - risk of harm - CONTACT CLA


    When I click option You are living in rented accommodation
    And I click option Harassment
    And I click option A partner expartner or family member
    And I click option YES you are not immediate risk of harm
    Then I verify I am on the contact civil legal advice page


  Scenario: In rented accommodation - harrasment - a partner or family member - no risk of harm - MEANS TEST


    When I click option You are living in rented accommodation
    And I click option Harassment
    And I click option A partner expartner or family member
    And I click option NO you are in immediate risk of harm
    Then I verify I am on the about me page


  Scenario: In rented accommodation - harrasment - someone else - NO MEANS TEST


    When I click option You are living in rented accommodation
    And I click option Harassment
    And I click option By someone else
    Then I verify I am on the A legal adviser may be able to help you page


  Scenario Outline: In rented accommodation - discrimination - age - over 18

    When I click option You are living in rented accommodation
    And I click option Discrimination
    And I click option By age
    And I click option 18 or over
    And I click option <situation>
    Then I verify I am on the <page>
    Examples:
      | situation                                       | page                                                     |
      | At work                                         | about me page                                            |
      | While you were using a service                  | about me page                                            |
      | At a private club                               | about me page                                            |
      | When someone was carrying out a public function | about me page                                            |
      | At university                                   | about me page                                            |
      | Other (debt discrimination problem)             | legal aid is not usually available for this problem page |


  Scenario: In rented accommodation - discrimination - age - under 18 - at work -  MEANS TEST


    When I click option You are living in rented accommodation
    And I click option Discrimination
    And I click option By age
    And I click option Under 18
    Then I verify I am on the contact civil legal advice page

  Scenario Outline: In rented accommodation - discrimination - disability

    When I click option You are living in rented accommodation
    And I click option Discrimination
    And I click Disability
    And I click disability discrimination <situation>
    Then I verify I am on the <page>
    Examples:
      | situation                                       | page                                                     |
      | at work                                         | about me page                                            |
      | at home                                         | about me page                                            |
      | while using a service                           | about me page                                            |
      | at a private club                               | about me page                                            |
      | when someone was carrying out a public function | about me page                                            |
      | at school or college                            | about me page                                            |
      | at university                                   | about me page                                            |
      | other                                           | legal aid is not usually available for this problem page |
