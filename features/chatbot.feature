Feature: This will test chat bot window and its functionality

  Scenario: Chat Bot window function
    Given I am on Haptik HomePage
    When I click on the chat bubble
    Then I validate the menu
    When I select view more
    When I select "Haptik Products" from chat options
    Then I verify chat message is "Tell me about Haptik's products"
    When I choose "Concierge Bot"
    Then I verify the given options after bot selection
    When I click on chat option "See an example"
    Then I verify the given options after choosing for example
    When I click on chat option "Other options"
    Then I verify chat message is "I would like to see some other options."
    When I click on the bottom Menu
    And I select view more
    And I select "Get a Chatbot" from chat options
    Then I verify chat message is "Hello! I am looking for a chatbot"
    And I verify chat window title is "Haptik is online"
    And I verify chat window subtitle is "World's Largest Conversational AI Platform"
    And I close chat window