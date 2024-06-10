
def check_counts(a_00, a_01, a_10, a_11):
    total_zeros = a_00 + a_01
    total_ones = a_10 + a_11
    if total_zeros == 0 and total_ones == 0:
        return "Impossible"
    if abs(total_zeros - total_ones) > 1:
        return "Impossible"
    
    if total_zeros >= total_ones:
        return "0" + "01" * a_01 + "0" * (a_00 - a_01)
    else:
        return "1" + "10" * a_10 + "1" * (a_11 - a_10)

if __name__ == "__main__":
    a_00, a_01, a_10, a_11 = map(int, input().split())
    result = check_counts(a_00, a_01, a_10, a_11)
    print(result)
