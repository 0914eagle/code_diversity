
def find_matching_string(a_00, a_01, a_10, a_11):
    total_length = a_00 + a_01 + a_10 + a_11
    if total_length == 0:
        print("Impossible")
        return

    if a_00 == 0 and a_11 == 0:
        if a_01 == 0 or a_10 == 0:
            print("Impossible")
            return

    result = []
    if a_00 > 0:
        result.append("0" * (a_00 + 1))
    if a_11 > 0:
        result.append("1" * (a_11 + 1))

    if a_01 > 0 and a_10 > 0:
        result.append("01" * min(a_01, a_10))
        a_01 -= min(a_01, a_10)
        a_10 -= min(a_01, a_10)

    if a_01 > 0:
        result.append("01" * a_01)
    if a_10 > 0:
        result.append("10" * a_10)

    final_result = "".join(result)[:total_length]
    print(final_result)

if __name__ == "__main__":
    a_00, a_01, a_10, a_11 = map(int, input().split())
    find_matching_string(a_00, a_01, a_10, a_11)
