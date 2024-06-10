
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
        s = "0" + "10" * a_10 + "1" * (a_01 - a_10)
    else:
        s = "1" + "01" * a_01 + "0" * (a_10 - a_01)
    
    print(s)

if __name__ == "__main__":
    a_00, a_01, a_10, a_11 = map(int, input().split())
    find_matching_string(a_00, a_01, a_10, a_11)
