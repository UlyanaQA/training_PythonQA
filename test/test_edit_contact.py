import time
from random import randrange
import random

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Temp_contact"))
    old_contacts = db.get_contact_list()
    random_contact = randrange(len(old_contacts))
    contact = Contact(firstname="Edited_firstname", lastname="Edited_lastname")
    contact.id = old_contacts[random_contact].id
    contact.lastname = old_contacts[random_contact].lastname
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[random_contact] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)