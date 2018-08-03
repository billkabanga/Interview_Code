import unittest
from pig_latin import word_converter

class TestPig_latin(unittest.TestCase):

    def test_word_is_converted(self):#method to test if the word is converted as expected
        word = 'will'
        assert word_converter(word) == 'illway'

        word = 'dog'
        assert word_converter(word) == 'ogday'

        word = 'category'
        assert word_converter(word) == 'ategorycay'

        word = 'chatter'
        assert word_converter(word) == 'atterchay'

        word = 'trash'
        assert word_converter(word) == 'ashtray'

        word = 'andela'
        assert word_converter(word) == 'andelaway'

        word = 'electrician'
        assert word_converter(word) == 'electricianway'
        
    def test_raise_error_for_integer(self):#method to test if error is raised for an integer.
        word = 55
        word = str(word)
        self.assertEqual(word_converter(word),'Strictly enter a word')   

if __name__ == '__main__':
    unittest.main()