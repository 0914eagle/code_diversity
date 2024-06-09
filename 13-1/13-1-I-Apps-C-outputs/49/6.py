
def get_distance(a, b):
    a_str = str(a)
    b_str = str(b)
    if len(a_str) < len(b_str):
        a_str = '0' * (len(b_str) - len(a_str)) + a_str
    elif len(b_str) < len(a_str):
        b_str = '0' * (len(a_str) - len(b_str)) + b_str
    distance = 0
    for i in range(len(a_str)):
        distance += abs(int(a_str[i]) - int(b_str[i]))
    return distance

def solve(a, b):
    total_distance = 0
    for i in range(a, b+1):
        for j in range(i+1, b+1):
            total_distance += get_distance(i, j)
    return total_distance % 1000000007

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solve(a, b))

