import unittest
from unittest import defaultTestLoader

def get_allcase():
    discover = unittest.defaultTestLoader.discover('./test_case',pattern='test*.py')
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_allcase())