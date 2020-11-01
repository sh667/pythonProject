import unittest,csv
from Calculator import Calculator
from CsvReader import CsvReader

class TestCalculator(unittest.TestCase):

    calculator = None
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator,Calculator)
    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    def tearDown(self):

        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator,Calculator)

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
    def test_divide(self):
         print('')
         print('******test_divide******')
         CsvReader.test_data_row_list = []
         test_data_file_path = CsvReader('./src/Division.csv').test_data_row_list
         print(test_data_file_path)
         print('Division loaded')
         for row in test_data_file_path:
             self.assertEqual(self.calculator.divide(float(row[0]), float(row[1])), float(row[2]))
    def test_square(self):
         print('')
         print('******test_square******')
         CsvReader.test_data_row_list = []
         test_data_file_path = CsvReader('./src/Square.csv').test_data_row_list
         print(test_data_file_path)
         print('Sqauer loaded')
         for row in test_data_file_path:
             self.assertEqual(self.calculator.square(float(row[0])), float(row[1]))
    def test_squareroot(self):
         print('')
         print('******test_squareroot******')
         CsvReader.test_data_row_list = []
         test_data_file_path = CsvReader('./src/SquareRoot.csv').test_data_row_list
         print(test_data_file_path)
         print('Sqauerroot loaded')
         for row in test_data_file_path:
             self.assertEqual(self.calculator.squareroot(float(row[0])), float(row[1]))


def build_test_suite():

    test_suite = unittest.TestSuite()
    test_suite.addTest(TestCalculator('test_instantiate_calculator'))
    test_suite.addTest(TestCalculator('test_minus'))
    test_suite.addTest(TestCalculator('test_plus'))
    test_suite.addTest(TestCalculator('test_multiple'))
    test_suite.addTest(TestCalculator('test_divide'))
    test_suite.addTest(TestCalculator('test_square'))
    test_suite.addTest(TestCalculator('test_squareroot'))
    return test_suite
def build_text_report():
    test_suite = build_test_suite()

    test_runner = unittest.TextTestRunner()

    test_runner.run(test_suite)

if __name__ == "__main__":
    build_text_report()

