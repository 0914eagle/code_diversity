
def validate_delimiters(L):
    opening_delimiters = ["(", "[", "{"]
    closing_delimiters = [")", "]", "}"]
    delimiter_stack = []
    for i, char in enumerate(L):
        if char in opening_delimiters:
            delimiter_stack.append(char)
        elif char in closing_delimiters:
            if not delimiter_stack or delimiter_stack[-1] != opening_delimiters[closing_delimiters.index(char)]:
                return char, i
            else:
                delimiter_stack.pop()
    if delimiter_stack:
        return "ok so far", -1
    else:
        return "ok so far", -1

