*** Settings ***
Library  rf.AddressBook
Library    Collections
Suite Setup    Init Fixture
Suite Teardown    Destroy Fixture

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  lastname1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Group  ${contact}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Contact List
    ${contact_for_editing}=  Random contact  ${old_list}
    ${contact_data}=  Create contact data  Edited_firstname  Edited_lastname  ${contact_for_editing}
    Edit Contact  ${contact_data}
    ${new_list}=  Get Contact List
    Remove values from list  ${old_list}  ${contact_for_editing}
    Append to list  ${old_list}  ${contact_data}
    Contact lists should be equal  ${new_list}  ${old_list}