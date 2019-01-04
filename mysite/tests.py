import unittest
from .count import Count
# Create your tests here.
class MyTest(unittest.TestCase) :
    def tearDown(self):
        print('test end')

    def  setUp(self):
        print('test start')

    @classmethod
    def tearDownClass(cls):
        print('all  down')

    @classmethod
    def setUpClass(cls):
        print('all  start')

    def test_add(self):
        self.Count = Count(2,4)
        self.assertEqual(self.Count.add(),5)


if __name__ == '__main__':
    unittest.main()
