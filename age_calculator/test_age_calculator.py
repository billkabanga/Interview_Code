import unittest
from age_calculator import ageCalculator

class TestAge_calculator(unittest.TestCase):

    def test_correct_age_is_calculated(self):
        birth_year = 1990
        assert ageCalculator(birth_year) == 28
    

if __name__ == '__main__':
    unittest.main()