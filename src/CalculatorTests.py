import unittest,csv
from Calculator import Calculator
from CsvReader import CsvReader

class TestCalculator(unittest.TestCase):

    calculator = None

    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    def tearDown(self):

        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')


    def test_minus(self):
         print('')
         print('******test_minus******')
         test_data_file_path=CsvReader('./src/Subtraction.csv').test_data_row_list
         print('Subtraction loaded')
         print(test_data_file_path)
         for row in test_data_file_path:
             self.assertEqual(self.calculator.minus(int(row[0]), int(row[1])), int(row[2]))

    def test_plus(self):
        print('')
        print('******test_plus******')
        CsvReader.test_data_row_list=[]
        test_data_file_path=CsvReader('./src/Addition.csv').test_data_row_list
        print('Addition loaded')
        print(test_data_file_path)
        for row in test_data_file_path:
            self.assertEqual(self.calculator.plus(int(row[0]), int(row[1])), int(row[2]))
    def test_multiple(self):
         print('')
         print('******test_multiple******')
         CsvReader.test_data_row_list = []
         test_data_file_path=CsvReader('./src/Multiplication.csv').test_data_row_list
         print('Multiplication loaded')
         print(test_data_file_path)
         for row in test_data_file_path:
             self.assertEqual(self.calculator.multiple(int(row[0]), int(row[1])), int(row[2]))


def build_test_suite():

    test_suite = unittest.TestSuite()

    test_suite.addTest(TestCalculator('test_minus'))
    test_suite.addTest(TestCalculator('test_plus'))
    test_suite.addTest(TestCalculator('test_multiple'))

    return test_suite
def build_text_report():
    test_suite = build_test_suite()

    test_runner = unittest.TextTestRunner()

    test_runner.run(test_suite)

if __name__ == "__main__":
    build_text_report()

