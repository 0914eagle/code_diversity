
def check_relation(y, sign, x, answer):
    if sign == '>=':
        return y >= x if answer == 'Y' else y < x
    elif sign == '<=':
        return y <= x if answer == 'Y' else y > x
    elif sign == '>':
        return y > x if answer == 'Y' else y <= x
    elif sign == '<':
        return y < x if answer == 'Y' else y >= x

def find_possible_y(n, queries):
    for y in range(-2*10**9, 2*10**9 + 1):
        valid = True
        for sign, x, answer in queries:
            if not check_relation(y, sign, x, answer):
                valid = False
                break
        if valid:
            return y
    return "Impossible"

if __name__ == "__main__":
    n = int(input())
    queries = []
    for _ in range(n):
        sign, x, answer = input().split()
        x = int(x)
        queries.append((sign, x, answer))
    
    result = find_possible_y(n, queries)
    print(result)