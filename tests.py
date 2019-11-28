import helper
from calc import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_total(self):
        """  Проверка калькулятора """
        
        total, discont_total = calc(count=1000, price=10, state='al')
        self.assertEqual(total, 9360.0)
        self.assertEqual(discont_total, 9000.0)
        total, discont_total = calc(count=2000, price=10.0, state='al')
        self.assertEqual(total, 18720.0)
        self.assertEqual(discont_total, 18000.0)

    def test_exception(self):
        """ Проверка исключений """
        
        with self.assertRaises(helper.ErrorCount):
            calc(count=0, price=10, state='al')
            
        with self.assertRaises(helper.ErrorCount):
            calc(count="", price=10, state='al')

        with self.assertRaises(helper.ErrorCount):
            calc(count="count", price=10, state='al')
            
        with self.assertRaises(helper.ErrorCount):
            calc(count=[1], price=10, state='al')
            
        with self.assertRaises(helper.ErrorPrice):
            calc(count=100, price=0, state='al')
        
        with self.assertRaises(helper.ErrorPrice):
            calc(count=100, price="", state='al')
        
        with self.assertRaises(helper.ErrorPrice):
            calc(count=100, price="price", state='al')
            
        with self.assertRaises(helper.ErrorPrice):
            calc(count=100, price=[1], state='al')
            
        with self.assertRaises(helper.ErrorState):
            calc(count=100, price=10, state='')
            
        with self.assertRaises(helper.ErrorState):
            calc(count=100, price=10, state=0)
            
        with self.assertRaises(helper.ErrorState):
            calc(count=100, price=10, state='state')


if __name__ == '__main__':
    unittest.main()