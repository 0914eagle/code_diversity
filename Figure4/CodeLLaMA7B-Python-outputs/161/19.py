def solve(s):
    
    new_string = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                new_string += i.upper()
            else:
                new_string += i.lower()
        else:
            new_string += i
    if new_string == "":
        return s[::-1]
    return new_string


if __name__ ==