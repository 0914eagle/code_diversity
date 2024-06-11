def fix_spaces(text):
    
    if not text:
        return text
    text = text.replace(' ', '_')
    text = text.replace('__', '-')
    if text[0] == '_':
        text = text[1:]
    return text


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces("Example"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1