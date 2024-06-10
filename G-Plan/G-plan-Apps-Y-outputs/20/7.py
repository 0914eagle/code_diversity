
def calculate_operations(n, t):
    if t == 1:
        return n
    elif t == 2:
        return 2 ** n
    elif t == 3:
        return n ** 4
    elif t == 4:
        return n ** 3
    elif t == 5:
        return n ** 2
    elif t == 6:
        return n * (n.bit_length())
    elif t == 7:
        return n

def check_time_limit(m, n, t):
    ops = calculate_operations(n, t)
    if ops <= m:
        return "AC"
    else:
        return "TLE"

if __name__ == "__main__":
    m, n, t = map(int, input().split())
    result = check_time_limit(m, n, t)
    print(result)
