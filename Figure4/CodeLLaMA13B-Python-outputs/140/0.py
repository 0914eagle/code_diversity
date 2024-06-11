def fix_spaces(text):
    
    if not text:
        return text
    text = text.replace(' ', '_')
    return text.replace('__', '-')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fix_spaces("") == "", "1st"
    assert fix_spaces("One") == "One", "2nd"
    assert fix_spaces("Two words") == "Two_words", "3rd"
    assert fix_spaces