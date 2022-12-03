fixture_check_document_existance = [
    '11-2',
    '2207 876234',
    '10006'
]

fixture_add_new_shelf = [
    ('5', ('5', True)),
    ('2', ('2', False))
]

fixture_delete_doc = [
    ('11-2', ('11-2', True)),
    ('00000', None),
    ('10006', ('10006', True))
]

fixture_get_doc_owner_name = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов')
]

fixture_get_doc_shelf = [
    ('11-2', '1'),
    ('2207 876234', '1'),
    ('10006', '2'),
    ('0000000', None)
]

fixture_remove_doc_from_shelf = [
    '11-2',
    '00000'
]

fixture_show_document_info = [
    ({"type": "a", "number": "1", "name": "AA"}, 'a "1" "AA"'),
    ({"type": "b", "number": "2", "name": "BB"}, 'b "2" "BB"'),
    ({"type": "c", "number": "3", "name": "CC"}, 'c "3" "CC"')
]
