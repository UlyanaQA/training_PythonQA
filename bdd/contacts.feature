Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact

  Examples:
  | firstname  | lastname  | email  |
  | firstname1 | lastname1 | email1 |
  | firstname2 | lastname2 | email2 |


Scenario Outline: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact

Scenario Outline: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname> and <email>
  When I edit the contact from the list
  Then the new contact list is equal to the old contact list with the edited contact

  Examples:
  | firstname  | lastname  | email  |
  | firstname_ | lastname_ | email_ |