# -*- coding: utf-8 -*-
# Test add contact. One fixture
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.create_new_contact(
        Contact(firstname="Test_first", middlename="Test_middle", lastname="Test_last", nickname="Nick",
                title="Test_title", company="SpaceX",
                address="The Earth", phone1="12345678", mobilephone="87654321", workphone="1234", fax="4321",
                email1="mozgulya@gmail.com",
                email2="test@ght.ru", email3="test@kil.com", site="space.ru", bday="6", bmonth="March",
                byear="1997", aday="7", amonth="March", ayear="2023",
                address2="The Earth", phone2="89217629999", notes="Some notes"))
    app.return_to_add_new()
    app.session.logout()
