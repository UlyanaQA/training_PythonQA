# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address():
    return random_string(20) + "," + random_string(20)


def random_phone():
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(4, 10))])


def random_email():
    domen = [".ru", ".org", ".com"]
    return random_string(10) + "@" + random_string(10) + random.choice(domen)


def random_site():
    domen = [".ru", ".org", ".com", "etu"]
    return random_string(10) + random.choice(domen)


testdata = [Contact(firstname=random_string(10), middlename=random_string(10),
                    lastname=random_string(10), nickname=random_string(10),
                    title=random_string(10), company=random_string(10),
                    address=random_address(), homephone=random_phone(),
                    mobilephone=random_phone(), workphone=random_phone(),
                    fax=random_phone(), email1=random_email(),
                    email2=random_email(), email3=random_email(),
                    site=random_site(), address2=random_address(),
                    secondaryphone=random_phone(), notes=random_string(20)) for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
