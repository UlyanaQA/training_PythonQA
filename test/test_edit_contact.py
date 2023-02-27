import time

from model.contact import Contact


def test_edit_firstname(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(firstname="old firstname"))
    app.contact.edit_first_contact(Contact(firstname="10000Edit_first"))


def test_edit_middlename(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(middlename="old middlename"))
    app.contact.edit_first_contact(Contact(middlename="1000Edit_middle"))


def test_edit_lastname(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(lastname="old lastname"))
    app.contact.edit_first_contact(Contact(lastname="100Edit_last"))


def test_edit_nickname(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(nickname="old nickname"))
    app.contact.edit_first_contact(Contact(nickname="1Edit_Nick"))


def test_edit_title(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(title="old title"))
    app.contact.edit_first_contact(Contact(title="1Edit_title"))


def test_edit_company(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(company="old company"))
    app.contact.edit_first_contact(Contact(company="1ED_SpaceX"))


def test_edit_address(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(address="old address"))
    app.contact.edit_first_contact(Contact(address="1The Mars"))


def test_edit_phone1(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(phone1="old phone"))
    app.contact.edit_first_contact(Contact(phone1="011111"))


def test_edit_mobilephone(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(mobilephone="old mobilephone"))
    app.contact.edit_first_contact(Contact(mobilephone="022222"))


def test_edit_workphone(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(workphone="old workphone"))
    app.contact.edit_first_contact(Contact(workphone="03333"))


def test_edit_fax(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(fax="old fax"))
    app.contact.edit_first_contact(Contact(fax="04444"))


def test_edit_email1(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(email1="old_email1@mail.gu"))
    app.contact.edit_first_contact(Contact(email1="1editmozgulya@gmail.com"))


def test_edit_email2(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(email2="old_email2@.ko"))
    app.contact.edit_first_contact(Contact(email2="1edittest@ght.ru"))


def test_edit_email3(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(email3="old_email3@.ko"))
    app.contact.edit_first_contact(Contact(email3="3333edittest@kil.com"))


def test_edit_site(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(site="old_site.ko"))
    app.contact.edit_first_contact(Contact(site="1space.com"))


def test_edit_bday(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(bday="1"))
    app.contact.edit_first_contact(Contact(bday="18"))


def test_edit_bmonth(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(bmonth="March"))
    app.contact.edit_first_contact(Contact(bmonth="May"))


def test_edit_byear(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(byear="1993"))
    app.contact.edit_first_contact(Contact(byear="1996"))


def test_edit_aday(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(aday="1"))
    app.contact.edit_first_contact(Contact(aday="5"))


def test_edit_amonth(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(amonth="March"))
    app.contact.edit_first_contact(Contact(amonth="April"))


def test_edit_ayear(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(ayear="1993"))
    app.contact.edit_first_contact(Contact(ayear="2022"))


def test_edit_address2(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(address2="Land"))
    app.contact.edit_first_contact(Contact(address2="1The Mars"))


def test_edit_phone2(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(phone2="147852"))
    app.contact.edit_first_contact(Contact(phone2="055555"))


def test_edit_notes(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(notes="hhhhhhh"))
    app.contact.edit_first_contact(Contact(notes="1Some changes"))
