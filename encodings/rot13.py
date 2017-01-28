'''Testing methods to encode text in rot13:
The maketrans method was the fastest, with 113 usec.
After him the fastest was the raw method, with 348 usec.
Lastly was the codecs.encode method of the default library with 5558 usec.
The tests were run on Debian 8 Jessie on an Intel Core i5-2467M, where the
phrase "42 is the Answer to the Ultimate Question of Life, The Universe,
and Everything" was encoded and decoded using each of the methods.
For more about rot13: https://en.wikipedia.org/wiki/ROT13'''

import codecs

def codecsrot13(phrase):
    return codecs.encode(phrase, 'rot_13')

def maketransrot13(phrase):
    '''The logic of rot13 is simple. Each letter is changed by the equivalent
    of 13 forward positions. You can do rot13 with maketrans, which creates a
    translation table, where the second string is the translation of the
    first. All the letters of the second string are the letters of the first
    string rotated in 13 forward positions.'''
    rot13table = str.maketrans(
		'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    )
    return phrase.translate(rot13table)

def rawrot13(phrase):
    '''The logic of the raw method is the same as that of maketrans, but the
    translation is make manually in a for loop, replacing the characters of
    the phrase in their equivalent 13 forward positions.'''
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot13_letters = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    encoded_phrase = ''
    for p in phrase:
        try:
            '''When the character is found in the table, its translation
            equivalent is added to the result.'''
            encoded_phrase += rot13_letters[ascii_letters.index(p)]
        except ValueError:
            '''If the character is not in the table, such as numbers and
            punctuations, it is added to the result without translation.'''
            encoded_phrase += p
    return encoded_phrase
