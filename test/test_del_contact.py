import random

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create_new(Contact(firstname="old firstname"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(random_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)