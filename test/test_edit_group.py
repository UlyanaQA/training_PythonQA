from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group3", header="test group3 header", footer="test group3 footer"))
    app.session.logout()
