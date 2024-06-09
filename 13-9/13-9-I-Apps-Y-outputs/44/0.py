
def is_code_hard_to_enter(code):
    if len(code) != 4:
        return "Bad"
    if code[1] == code[2] or code[2] == code[3]:
        return "Bad"
    return "Good"

