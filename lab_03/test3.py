import unittest
from group import GroupList
from fim import FileManager
from student import Student
import os
import io
from unittest.mock import patch

class TestLab(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_data.csv"
        self.file_path = os.path.join(os.path.dirname(__file__), self.file_name)
        self.group_list = GroupList()
        self.file_manager = FileManager()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_student(self):
        student = Student("John", "123456789", "145", "A1")
        self.group_list.add_student(student)
        self.assertEqual(len(self.group_list.student_list), 1)
        self.assertEqual(self.group_list.student_list[0].name, "John")

    def test_delete_student(self):
        student = Student("Alice", "987654321", "012", "B2")
        self.group_list.add_student(student)
        self.group_list.delete_student("Alice")
        self.assertEqual(len(self.group_list.student_list), 0)

    def test_update_student_with_mocked_input(self):
        student = Student("Bob", "555555555", "140", "C3")
        self.group_list.add_student(student)
        with patch("builtins.input", side_effect=["1", "Robert"]):
            self.group_list.update_student("Bob")
        self.assertEqual(self.group_list.student_list[0].name, "Robert")

    def test_print_all_students(self):
        student1 = Student("Anna", "111111111", "142", "D4")
        student2 = Student("Eva", "222222222", "131", "E5")
        self.group_list.add_student(student1)
        self.group_list.add_student(student2)
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.group_list.print_all_students()
        output = mock_stdout.getvalue()
        self.assertIn("Student name is Anna", output)
        self.assertIn("Student name is Eva", output)

    def test_load_and_save_data(self):
        student1 = Student("Alice", "111111111", "142", "D4")
        student2 = Student("Bob", "222222222", "131", "E5")
        self.group_list.add_student(student1)
        self.group_list.add_student(student2)
        self.file_manager.save_data_to_csv(self.file_path, self.group_list)
        loaded_group_list = GroupList()
        self.file_manager.load_and_sort_data(self.file_path, loaded_group_list)
        self.assertEqual(len(loaded_group_list.student_list), 2)
        self.assertEqual(loaded_group_list.student_list[0].name, "Alice")
        self.assertEqual(loaded_group_list.student_list[1].name, "Bob")

if __name__ == '__main__':
    unittest.main()
    