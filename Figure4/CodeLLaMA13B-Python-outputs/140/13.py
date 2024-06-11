def fix_spaces(text):
    
    if not text:
        return text
    if len(text) == 1:
        return text.replace(" ", "_")
    if text[0] == " ":
        text = "_" + text[1:]
    if text[-1] == " ":
        text = text[:-1] + "_"
    return text.replace("  ", "-").replace(" ", "_")


if __name__ == '__main__':
    print("Example:")
    print(fix_spaces(""))

    # These "asserts" are used for