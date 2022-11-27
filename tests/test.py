import unittest
from speciallecture.sample import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter('tests/data.csv')
        line = printer.read()
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter('tests/data.csv')
        line = printer.read()
        self.assertEqual("value2B", line[1][1])

    def test_read3(self):
        try:
            printer = CSVPrinter('tests/none.csv')
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            print('FileNotFoundError',e)

        # with self.assertRaises(FileNotFoundError) as e:
        #     printer = CSVPrinter('sample.csv')
        #     line = printer.read()
        #     print(line)