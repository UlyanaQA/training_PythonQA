from random import randrange

from model.group import Group


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Temp_group", header="Temp_header", footer="Temp_footer"))
    old_groups = db.get_group_list()
    group = Group(name="edited_group_name", header="edited_header", footer="edited_footer")
    random_group = randrange(len(old_groups))
    group.id = old_groups[random_group].id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[random_group] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(app.group.clean_group_name, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)