
def get_input():
    a_00, a_01, a_10, a_11 = map(int, input().split())
    return a_00, a_01, a_10, a_11

def is_possible(a_00, a_01, a_10, a_11):
    if a_00 + a_01 + a_10 + a_11 == 0:
        return True
    if a_00 + a_01 + a_10 + a_11 == 1:
        return False
    if a_00 + a_01 + a_10 + a_11 == 2:
        if a_00 == 1 and a_01 == 1:
            return True
        if a_10 == 1 and a_11 == 1:
            return True
        return False
    if a_00 + a_01 + a_10 + a_11 == 3:
        if a_00 == 1 and a_01 == 2:
            return True
        if a_10 == 2 and a_11 == 1:
            return True
        return False
    if a_00 + a_01 + a_10 + a_11 == 4:
        if a_00 == 1 and a_01 == 3:
            return True
        if a_10 == 3 and a_11 == 1:
            return True
        return False
    return False

def find_string(a_00, a_01, a_10, a_11):
    if is_possible(a_00, a_01, a_10, a_11):
        string = ""
        if a_00 == 1:
            string += "0"
        if a_01 == 1:
            string += "1"
        if a_10 == 1:
            string += "0"
        if a_11 == 1:
            string += "1"
        return string
    return "Impossible"

if __name__ == '__main__':
    a_00, a_01, a_10, a_11 = get_input()
    print(find_string(a_00, a_01, a_10, a_11))

