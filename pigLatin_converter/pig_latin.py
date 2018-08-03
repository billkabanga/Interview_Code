"""My Pig Latin Converter"""
pyp = 'ay' 
pyp_1 = 'way'
consonant = ['b', 'c', 'd', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 
's', 't', 'v', 'w', 'x', 'y', 'z' ]#list of consonants
vowel = ['a','e','i','o','u']#list of vowels

def word_converter(word): #function word_converter takes an arg word.
    
    if len(word) > 0 and word.isalpha():#conditional loop to test if input is a word.
        my_word = word.lower()
        first = my_word[0]
        second = my_word[1]
        if first in consonant and second in consonant :
            new_word = my_word[2:] + my_word[0] + my_word[1] + pyp
            print (new_word)
        elif first in consonant:
            new_word = my_word[1:] + my_word[0] + pyp
            print (new_word)
        elif first in vowel:
            new_word = my_word + pyp_1
            print (new_word) 
        elif first not in consonant:
            new_word = my_word
            print ('Choose another word')
            
    else:
        print ('Strictly enter a word')
        return ('Strictly enter a word')
    return (new_word)
    
if __name__ == '__main__':
    word = input("Enter a word: " )
    word_converter(word)