from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.is_list_empty():
        app.contact.create_new(Contact(firstname="old firstname"))
    app.contact.delete_first_contact()