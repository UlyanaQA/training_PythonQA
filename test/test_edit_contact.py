import time
from random import randrange
import random

import allure

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="Temp_contact"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        random_contact = randrange(len(old_contacts))
    with allure.step('When I edit a contact %s from the list' % random_contact):
        contact = Contact(firstname="Edited_firstNAME11", lastname="Edited_lastNAME11")
        contact.id = old_contacts[random_contact].id
        contact.lastname = old_contacts[random_contact].lastname
        app.contact.edit_contact_by_id(contact.id, contact)
    with allure.step('Then the new contact list is equal to the old contact list with the edited contact'):
        new_contacts = db.get_contact_list()
        old_contacts[random_contact] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)