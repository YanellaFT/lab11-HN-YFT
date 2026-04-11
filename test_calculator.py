# https://github.com/YanellaFT/lab11-HN-YFT
# Partner 1: Hai Nguyen
# Partner 2: Yanella Fernandez Teusen

import unittest
from calculator import mul, div, logarithm, hypotenuse, square_root, add, subtract


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        add(2, 4)
        add(-1, -1)
        add(4, -3)

    def test_subtract(self): # 3 assertions
        subtract(2, 4)
        subtract(-1, -1)
        subtract(4, -3)
# ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(0,5), 0)
        self.assertEqual(mul(-2,3),-6)
        self.assertEqual(mul(2.5,2), 5.0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10), 5.0)
        self.assertEqual(div(20,4),0.2)
        self.assertEqual(div(-1,-5), 5.0)
        self.assertRaises(ZeroDivisionError, div, 0, 5)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        # with self.assertRaises(ValueError):
        logarithm(3, 2)
        logarithm(5, 8)
        logarithm(100, 100)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0,5)
            logarithm(1,4)
            logarithm(2,-1)
        self.assertEqual(logarithm(2,4),2)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5.0)
        self.assertEqual(hypotenuse(0, 5), 5.0)
        self.assertAlmostEqual(hypotenuse(1,1), 1.414, places=3)
    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(0),0.0)
        self.assertAlmostEqual(square_root(2), 1.414, places=3)
        self.assertRaises(ValueError, square_root, -1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
