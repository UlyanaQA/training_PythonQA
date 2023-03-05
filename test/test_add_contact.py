# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(
        Contact(firstname="33Test_first", middlename="Test_middle", lastname="Test_last", nickname="Nick",
                title="Test_title", company="SpaceX",
                address="The Earth", phone1="12345678", mobilephone="87654321", workphone="1234", fax="4321",
                email1="mozgulya@gmail.com",
                email2="test@ght.ru", email3="test@kil.com", site="space.ru", bday="16", bmonth="March",
                byear="1999", aday="17", amonth="May", ayear="2021",
                address2="The Earth", phone2="89217629999", notes="Some notes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)