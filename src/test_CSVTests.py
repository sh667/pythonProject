import unittest
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/employee_birthday.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_class('person')
        self.assertIsInstance(people, list)

if __name__ == '__main__':
    unittest.main()