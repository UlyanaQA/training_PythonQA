import random

import allure

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_group_list()) == 0:
            app.contact.create_new(Contact(firstname="old firstname"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        random_contact = random.choice(old_contacts)
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(random_contact.id)
    with allure.step('Then the new contact list is equal to the old contact list without the deleted contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(random_contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.id_or_max)