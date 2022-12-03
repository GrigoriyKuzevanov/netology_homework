import unittest
import myapp
import fixtures
from unittest.mock import patch
from parameterized import parameterized


class TestApp1(unittest.TestCase):
    @parameterized.expand(fixtures.fixture_get_doc_owner_name)
    @patch('builtins.input')
    def test_get_doc_owner_name(self, fixtures_input, result, mock_input):
        mock_input.return_value = fixtures_input
        self.assertEqual(myapp.get_doc_owner_name(), result)

    @parameterized.expand(fixtures.fixture_check_document_existance)
    def test_check_document_existance(self, number):
        self.assertTrue(myapp.check_document_existance(number))

    @parameterized.expand(fixtures.fixture_add_new_shelf)
    @patch('builtins.input')
    def test_add_new_shelf(self, fixtures_input, result, mock_input):
        mock_input.return_value = fixtures_input
        self.assertEqual(myapp.add_new_shelf(), result)

    @parameterized.expand(fixtures.fixture_get_doc_shelf)
    @patch('builtins.input')
    def test_get_doc_shelf(self, doc_number, result, mock_input):
        mock_input.return_value = doc_number
        self.assertEqual(myapp.get_doc_shelf(), result)

    @patch('builtins.input', side_effect=['11-2', '3'])
    def test_move_doc_to_shelf(self, mock_inputs):
        result = f'Документ номер "11-2" был перемещен на полку номер "3"'
        self.assertEqual(myapp.move_doc_to_shelf(), result)

    @parameterized.expand(fixtures.fixture_remove_doc_from_shelf)
    def test_remove_doc_from_shelf(self, doc_number):
        self.assertEqual(myapp.remove_doc_from_shelf(doc_number), True)

    @parameterized.expand(fixtures.fixture_show_document_info)
    def test_show_document_info(self, document, result):
        self.assertEqual(myapp.show_document_info(document), result)

    def test_get_all_doc_owners_names(self):
        result = {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}
        self.assertEqual(myapp.get_all_doc_owners_names(), result)


class TestApp2(unittest.TestCase):
    @patch('builtins.input', side_effect=['10011', 'test type', 'test name', '2'])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(myapp.add_new_doc(), '2')

    @parameterized.expand(fixtures.fixture_delete_doc)
    @patch('builtins.input')
    def test_delete_doc(self, number, result, mock_input):
        mock_input.return_value = number
        self.assertEqual(myapp.delete_doc(), result)


