
def find_matching_string(a_00, a_01, a_10, a_11):
    total_length = a_00 + a_01 + a_10 + a_11
    if total_length == 0:
        print("Impossible")
        return

    if a_00 == 0 and a_11 == 0:
        if a_01 == 0:
            print("0" * total_length)
        elif a_10 == 0:
            print("1" * total_length)
        else:
            print("Impossible")
    elif abs(a_01 - a_10) > 1:
        print("Impossible")
    else:
        if a_01 > a_10:
            start_with_one = True
        else:
            start_with_one = False

        if start_with_one:
            result = "1"
            a_10 -= 1
        else:
            result = "0"
            a_01 -= 1

        while a_00 > 0 or a_01 > 0 or a_10 > 0 or a_11 > 0:
            if start_with_one:
                if result[-1] == "1":
                    if a_01 > 0:
                        result += "0"
                        a_01 -= 1
                    else:
                        result += "1"
                        a_11 -= 1
                else:
                    if a_10 > 0:
                        result += "1"
                        a_10 -= 1
                    else:
                        result += "0"
                        a_00 -= 1
            else:
                if result[-1] == "0":
                    if a_10 > 0:
                        result += "1"
                        a_10 -= 1
                    else:
                        result += "0"
                        a_00 -= 1
                else:
                    if a_01 > 0:
                        result += "0"
                        a_01 -= 1
                    else:
                        result += "1"
                        a_11 -= 1

        print(result)


if __name__ == "__main__":
    a_00, a_01, a_10, a_11 = map(int, input().split())
    find_matching_string(a_00, a_01, a_10, a_11)
