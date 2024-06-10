
def check_relation(y, sign, x):
    if sign == ">":
        return y > x
    elif sign == "<":
        return y < x
    elif sign == ">=":
        return y >= x
    elif sign == "<=":
        return y <= x

def find_possible_y(n, queries):
    for y in range(-2*10**9, 2*10**9 + 1):
        valid = True
        for query in queries:
            sign, x, answer = query
            x = int(x)
            if not check_relation(y, sign, x) == (answer == "Y"):
                valid = False
                break
        if valid:
            return y
    return "Impossible"

if __name__ == "__main__":
    n = int(input())
    queries = [input().split() for _ in range(n)]
    result = find_possible_y(n, queries)
    print(result)
