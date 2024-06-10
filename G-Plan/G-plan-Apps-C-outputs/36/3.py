
def find_matching_string(a_00, a_01, a_10, a_11):
    total_length = a_00 + a_01 + a_10 + a_11
    if total_length == 0:
        print("Impossible")
        return

    if a_00 == 0 and a_11 == 0:
        if a_01 > 0 and a_10 > 0:
            print("Impossible")
            return

    if abs(a_01 - a_10) > 1:
        print("Impossible")
        return

    if a_01 > a_10:
        start_with_0 = True
    else:
        start_with_0 = False

    result = ""
    if start_with_0:
        result += "0"
        a_01 -= 1
    else:
        result += "1"
        a_10 -= 1

    while a_01 > 0 and a_10 > 0:
        if start_with_0:
            result += "1"
            result += "0"
        else:
            result += "0"
            result += "1"
        a_01 -= 1
        a_10 -= 1

    if a_01 > 0:
        result += "1" * a_01
    if a_10 > 0:
        result = "0" * a_10 + result

    print(result)

if __name__ == "__main__":
    a_00, a_01, a_10, a_11 = map(int, input().split())
    find_matching_string(a_00, a_01, a_10, a_11)
