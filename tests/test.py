import unittest

class DummyTest(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(1, 1)
    
    def test_dummy2(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()