
def is_valid_string(s):
    if len(s) != n:
        return False
    for i in range(n):
        if s[i] not in ["a", "b", "c"]:
            return False
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            return False
    for i in range(n - 2):
        if s[i] == "c" and s[i + 1] == "a":
            return False
    return True

def find_string():
    for s in itertools.permutations("abc", n):
        if is_valid_string(s):
            return "".join(s)
    return None

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    if not is_valid_graph(edges):
        print("No")
    else:
        s = find_string()
        if s:
            print("Yes")
            print(s)
        else:
            print("No")

if __name__ == '__main__':
    main()

