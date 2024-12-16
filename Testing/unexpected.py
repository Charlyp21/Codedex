import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
  
  def Test_get_sqrt(self):
    self.assertEqual(get_sqrt(144), 12)
    
  def test_sqr_negative(self):  
    with self.assertRaises(ValueError):
      self.assertEqual(get_sqrt(-9), 12)

  def test_divide(self):
    self.assertEqual(divide(144,12), 12)

  def test_divide_zero(self):
    with self.assertRaises(ZeroDivisionError):
      self.assertEqual(divide(3, 0), 3)

if __name__ == '__main__':
  unittest.main()