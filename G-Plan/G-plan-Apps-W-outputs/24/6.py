
def check_relation(x, sign, answer, y):
    if sign == ">=":
        return y >= x if answer == "Y" else y < x
    elif sign == "<=":
        return y <= x if answer == "Y" else y > x
    elif sign == ">":
        return y > x if answer == "Y" else y <= x
    elif sign == "<":
        return y < x if answer == "Y" else y >= x

def find_possible_y(n, queries):
    for y in range(-2*10**9, 2*10**9 + 1):
        valid = True
        for query in queries:
            sign, x, answer = query
            if not check_relation(x, sign, answer, y):
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
