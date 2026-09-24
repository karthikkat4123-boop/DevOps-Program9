import unittest
from Calculator import Add

class TestCalculator(unittest.TestCase):
    
    
    def test_positive_number(self):
        self.assertEqual(Add(3, 4), 7) 

    def test_negative_number(self):
        self.assertEqual(Add(2, -5), -3) 

    def test_zero(self):
        self.assertEqual(Add(0, 4), 4)  

    def test_both_zero(self):
        self.assertEqual(Add(0, 0), 0)  

# 3. Fixed double underscores and added the correct colon
if __name__ == '__main__':
    unittest.main()
