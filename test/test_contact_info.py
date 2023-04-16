import re
from random import randrange

from model.contact import Contact


def test_contact_info_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == \
           app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_contacts_info_on_homepage_and_db(app, db):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Temp_firstname", lastname="Temp_lastname", homephone="123",
                                       email1="tempmail@test.com", address="The Earth"))
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_homepage)):
        hp_contact = contacts_from_homepage[i]
        db_contact = contacts_from_db[i]
        assert hp_contact.firstname == db_contact.firstname
        assert hp_contact.lastname == db_contact.lastname
        assert hp_contact.address == db_contact.address
        assert hp_contact.all_phones_from_home_page == merge_phones_like_on_home_page(db_contact)
        assert hp_contact.all_emails_from_home_page == merge_emails_like_on_home_page(db_contact)
    print("Successfully verified %s Homepage contacts and Database contacts" % str(len(contacts_from_homepage)))


def clear(s):
    return re.sub("[- ()]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email1, contact.email2, contact.email3])))


"""def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone"""
