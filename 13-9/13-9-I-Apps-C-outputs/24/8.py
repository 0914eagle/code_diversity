
def is_rooted_tree(c_values):
    n = len(c_values)
    if n == 1:
        return True
    if n == 2:
        return c_values[0] + c_values[1] == 2
    if n == 3:
        return c_values[0] + c_values[1] + c_values[2] == 3 and c_values[0] != c_values[1] != c_values[2]
    if n == 4:
        return c_values[0] + c_values[1] + c_values[2] + c_values[3] == 6 and c_values[0] != c_values[1] != c_values[2] != c_values[3]
    return False

def has_rooted_tree(c_values):
    for i in range(len(c_values)):
        if is_rooted_tree(c_values[:i]):
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    c_values = list(map(int, input().split()))
    print("YES") if has_rooted_tree(c_values) else print("NO")

