"""my unit test for the age calculator"""
import unittest
from age_calculator import ageCalculator

class TestAge_calculator(unittest.TestCase):

    def test_correct_age_is_calculated(self):
        birth_year = 1990
        assert ageCalculator(birth_year) == 28

    def test_year_less_than_expected(self):#method to test if a year below 1900 is supplied as input.
        birth_year = 1800
        self.assertEqual(ageCalculator(birth_year), 'Enter valid year' )
    
    
if __name__ == '__main__':
    unittest.main()