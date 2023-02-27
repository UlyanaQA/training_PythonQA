from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="Edit_contact1", middlename="Edit_middle", lastname="Edit_last", nickname="Edit_Nick",
                title="Edit_title", company="ED_SpaceX",
                address="The Mars", phone1="111110", mobilephone="222220", workphone="33330", fax="44440",
                email1="editmozgulya@gmail.com",
                email2="edittest@ght.ru", email3="edittest@kil.com", site="space.com", bday="7", bmonth="April",
                byear="1998", aday="8", amonth="May", ayear="2024",
                address2="The Mars", phone2="55555", notes="Some changes"))
    app.session.logout()
