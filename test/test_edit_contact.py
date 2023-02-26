import time

from model.contact import Contact


def test_edit_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="100Edit_first"))


def test_edit_middlename(app):
    app.contact.edit_first_contact(Contact(middlename="100Edit_middle"))


def test_edit_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="100Edit_last"))


def test_edit_nickname(app):
    app.contact.edit_first_contact(Contact(nickname="1Edit_Nick"))


def test_edit_title(app):
    app.contact.edit_first_contact(Contact(title="1Edit_title"))


def test_edit_company(app):
    app.contact.edit_first_contact(Contact(company="1ED_SpaceX"))


def test_edit_address(app):
    app.contact.edit_first_contact(Contact(address="1The Mars"))


def test_edit_phone1(app):
    app.contact.edit_first_contact(Contact(phone1="011111"))


def test_edit_mobilephone(app):
    app.contact.edit_first_contact(Contact(mobilephone="022222"))


def test_edit_workphone(app):
    app.contact.edit_first_contact(Contact(workphone="03333"))


def test_edit_fax(app):
    app.contact.edit_first_contact(Contact(fax="04444"))


def test_edit_email1(app):
    app.contact.edit_first_contact(Contact(email1="1editmozgulya@gmail.com"))


def test_edit_email2(app):
    app.contact.edit_first_contact(Contact(email2="1edittest@ght.ru"))


def test_edit_email3(app):
    app.contact.edit_first_contact(Contact(email3="1edittest@kil.com"))


def test_edit_site(app):
    app.contact.edit_first_contact(Contact(site="1space.com"))


def test_edit_bday(app):
    app.contact.edit_first_contact(Contact(bday="18"))


def test_edit_bmonth(app):
    app.contact.edit_first_contact(Contact(bmonth="May"))


def test_edit_byear(app):
    app.contact.edit_first_contact(Contact(byear="1996"))


def test_edit_aday(app):
    app.contact.edit_first_contact(Contact(aday="5"))


def test_edit_amonth(app):
    app.contact.edit_first_contact(Contact(amonth="April"))


def test_edit_ayear(app):
    app.contact.edit_first_contact(Contact(ayear="2022"))


def test_edit_address2(app):
    app.contact.edit_first_contact(Contact(address2="1The Mars"))


def test_edit_phone2(app):
    app.contact.edit_first_contact(Contact(phone2="055555"))


def test_edit_notes(app):
    app.contact.edit_first_contact(Contact(notes="1Some changes"))
