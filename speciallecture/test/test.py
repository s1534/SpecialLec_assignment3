import unittest
from speciallecture.sample import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        file = 'data.csv'
        printer = CSVPrinter(file)
        line = printer.read()
        self.assertEqual(3, len(line))

    def test_read2(self):
        file = 'data.csv'
        printer = CSVPrinter(file)
        line = printer.read()
        self.assertEqual("value2B", line[1][1])

    def test_read3(self):
        try:
            file = 'none.csv'
            printer = CSVPrinter(file)
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            print('FileNotFoundError',e)
