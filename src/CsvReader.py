import unittest, csv
from Calculator import Calculator
class CsvReader:
    test_data_file_path =None
    test_data_row_list = []
    def __init__(self, test_data_file_path):
        global test_data_file_object, test_data_row_list
        test_data_file_object = open(test_data_file_path, 'r')
        csv_reader = csv.reader(test_data_file_object, delimiter=',')
        for row in csv_reader:
            self.test_data_row_list.append(row)
            print('open and load data from test_data.csv complete.')
            pass


    def close_test_data_file(self):
        global test_data_file_object
        if test_data_file_object is not None:
            test_data_file_object.close()
            test_data_file_object = None
            print('close file test_data.csv complete.')