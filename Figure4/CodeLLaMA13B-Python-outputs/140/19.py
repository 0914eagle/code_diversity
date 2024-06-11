def fix_spaces(text):
    
    if text == "":
        return ""
    if text[0] == " ":
        text = "_" + text[1:]
    if text[-1] == " ":
        text = text[:-1] + "_"
    if "  " in text:
        text = text.replace("  ", "-")
    if "__" in text:
        text = text.replace("__", "_")
    if "--" in text:
        text = text.replace("--", "-")
    return text


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces(""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert fix_spaces("") == ""
    assert fix_spaces("One") == "One"
    assert fix_spaces("One Two") == "One_Two"
    assert fix_spaces(" One Two ") == "_One_Two_"
    assert fix_spaces(" One  Two ") == "_One-Two_"
    assert fix_spaces(" One    Two ") == "_One-_Two_"
    assert fix_spaces(" One        Two ") == "_One-----Two_"
    print("Coding complete? Click 'Check' to earn cool rewards!")
