
def check_relation(y, sign, x, answer):
    if sign == ">":
        return y > x if answer == "Y" else y <= x
    elif sign == "<":
        return y < x if answer == "Y" else y >= x
    elif sign == ">=":
        return y >= x if answer == "Y" else y < x
    elif sign == "<=":
        return y <= x if answer == "Y" else y > x

def find_possible_y(n, queries):
    for y in range(-2*10**9, 2*10**9+1):
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
    queries = [input().split() for _ in range(n)]
    queries = [(query[0], int(query[1]), query[2]) for query in queries]
    
    result = find_possible_y(n, queries)
    print(result)
