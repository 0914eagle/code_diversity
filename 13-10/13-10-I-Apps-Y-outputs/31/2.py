
def get_next_day(S):
    next_day = ""
    for char in S:
        if char == "2":
            next_day += "22"
        elif char == "3":
            next_day += "333"
        elif char == "4":
            next_day += "4444"
        elif char == "5":
            next_day += "55555"
        elif char == "6":
            next_day += "666666"
        elif char == "7":
            next_day += "7777777"
        elif char == "8":
            next_day += "88888888"
        elif char == "9":
            next_day += "999999999"
        else:
            next_day += char
    return next_day

def get_string_after_days(S, days):
    current_day = S
    for _ in range(days):
        current_day = get_next_day(current_day)
    return current_day

def get_kth_char(S, K):
    current_day = 1
    while len(get_string_after_days(S, current_day)) < K:
        current_day += 1
    return get_string_after_days(S, current_day)[K-1]

if __name__ == '__main__':
    S = input()
    K = int(input())
    print(get_kth_char(S, K))

