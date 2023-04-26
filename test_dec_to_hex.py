import unittest
import dec_to_hex as dh

class d2hTestCase(unittest.TestCase):
    def test_d2h1(self):
        answer = dh.decimal_to_hex(100)
        self.assertEqual(answer, '64')
    
    def test_d2h1(self):
        answer = dh.decimal_to_hex(1)
        self.assertEqual(answer, '1')

if __name__=='__main__':
    unittest.main()