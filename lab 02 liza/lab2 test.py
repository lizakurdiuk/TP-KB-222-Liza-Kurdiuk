import unittest
import csv
import os
import io
from unittest.mock import patch
from io import StringIO
from lab2 import *

class TestLab2(unittest.TestCase):

    def setUp(self):
        self.student_list = [
            {"name": "Alice", "phone": "123456789", "specialty": "CS", "group": "A"},
            {"name": "Zak", "phone": "987654321", "specialty": "IT", "group": "B"}
        ]

    def load_and_sort_data(file_name):
        try:
            with open(file_name, 'r') as file:
                reader = csv.DictReader(file)
                student_list = sorted([row for row in reader], key=lambda x: x['name'])
            print("Data loaded successfully from", file_name)
            return student_list
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")
            return []
        except Exception as e:
            print("Error loading data:", str(e))
            return []

    def test_save_data_to_csv(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            save_data_to_csv('lab-02/test_data.csv', self.student_list)
            self.student_list = load_and_sort_data('lab-02/test_data.csv')
        self.assertIn('Data saved successfully to lab-02/test_data.csv', mock_stdout.getvalue().strip())
        self.assertIn('Data loaded successfully from lab-02/test_data.csv', mock_stdout.getvalue().strip())
        expected_sorted_list = sorted(self.student_list, key=lambda x: x['name'])
        self.assertEqual(self.student_list, expected_sorted_list)

    @patch('builtins.input', side_effect=['John', '123456789', 'IT', 'C'])
    def test_add_new_element(self, mock_input):
        add_new_element(self.student_list)
        self.assertEqual(len(self.student_list), 3)
        self.assertEqual(self.student_list[1]['name'], 'John')

    @patch('builtins.input', side_effect=['Alice', '2', 'NewValue', '3', 'UpdatedGroup'])
    def test_update_element(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            update_element(self.student_list)
            self.student_list = sorted(self.student_list, key=lambda x: x['name'])
        self.assertIn('Student information has been updated', mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['Alice'])
    def test_delete_element(self, mock_input):
        delete_element(self.student_list)
        self.student_list = sorted(self.student_list, key=lambda x: x['name'])
        self.assertEqual(len(self.student_list), 1)
        self.assertNotIn('Alice', [student['name'] for student in self.student_list])

if __name__ == '__main__':
    unittest.main()

    