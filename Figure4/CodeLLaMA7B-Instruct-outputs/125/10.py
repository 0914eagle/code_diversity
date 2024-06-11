

def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    words = txt.split()
    if words:
        return words
    else:
        commas = txt.count(',')
        if commas:
            return txt.split(',')
        else:
            lowercase_letters = [chr(i) for i in range(97, 123)]
            odd_letters = [letter for i, letter in enumerate(lowercase_letters) if i % 2 == 1]
            return len(odd_letters)

