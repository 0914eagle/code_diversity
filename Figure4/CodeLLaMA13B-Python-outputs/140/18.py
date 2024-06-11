def fix_spaces(text):
    
    if text == "":
        return ""
    if text[0] == " ":
        return "_" + fix_spaces(text[1:])
    if text[0] != " ":
        if text[1] == " ":
            if text[2] == " ":
                return text[0] + "-" + fix_spaces(text[3:])
            else:
                return text[0] + "_" + fix_spaces(text[2:])
        else:
            return text[0] + fix_spaces(text[1:])


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces(""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert fix_spaces("") == ""
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces(" o  ") == "_o_-"
    assert fix_spaces("o   o") == "o__o"
    assert fix_spaces("o    o") == "o---o"
    print("Coding complete? Click 'Check' to earn cool rewards!")
