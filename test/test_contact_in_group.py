from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Temp_group"))
    random_group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(random_group)) == 0:
        app.contact.create_new(Contact(firstname="Temp_contact"))
    random_contact = random.choice(orm.get_contacts_not_in_group(random_group))
    app.contact.add_contact_to_group(random_contact, random_group)
    assert random_contact in orm.get_contacts_in_group(random_group)


def test_delete_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Temp_group"))
    random_group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new(Contact(firstname="Temp_contact"))
    if len(orm.get_contacts_in_group(random_group)) == 0:
        random_contact = random.choice(orm.get_contacts_not_in_group(random_group))
        app.contact.add_contact_to_group(random_contact, random_group)
        assert random_contact in orm.get_contacts_in_group(random_group)
    random_contact_for_del = random.choice(orm.get_contacts_in_group(random_group))
    app.contact.delete_contact_from_group(random_contact_for_del, random_group)
    assert random_contact_for_del not in orm.get_contacts_in_group(random_group)
    assert random_contact_for_del in orm.get_contacts_not_in_group(random_group)