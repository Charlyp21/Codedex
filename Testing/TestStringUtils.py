import unittest
from stringutils import reverse_string as rs
from stringutils import capitalize_string as cs
from stringutils import is_capitalized as isc

text = 'charly'

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        result = rs(text)
        self.assertEqual(text[::-1], result)
    
    def test_capitalize_string(self):
        result = cs(text)
        self.assertEqual(text.capitalize(), result)
    
    def test_is_capitalized(self):
        result = isc(text)
        self.assertFalse(result)
    
if __name__ == '__main__':
    unittest.main()