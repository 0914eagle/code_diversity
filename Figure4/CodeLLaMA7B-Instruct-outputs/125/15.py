

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
            lowercase = [chr(i) for i in range(97, 123)]
            count = 0
            for char in txt:
                if char.islower():
                    count += lowercase.index(char) % 2
            return count

