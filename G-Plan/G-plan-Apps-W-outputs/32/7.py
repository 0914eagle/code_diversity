
def calculate_xor_sum(u, v):
    if u > v or (u - v) % 2 != 0:
        return None

    xor_val = (u + v) // 2
    sum_val = (v - u) // 2

    if xor_val == 0:
        return [0] * sum_val

    res = []
    for i in range(61):
        if xor_val & (1 << i):
            res.append(1 << i)

    if sum(res) == sum_val:
        return res
    return None

def find_shortest_array(u, v):
    if u == 0 and v == 0:
        print(0)
        return

    for n in range(1, 62):
        res = calculate_xor_sum(u, v)
        if res:
            print(len(res))
            print(*res)
            return

    print(-1)

if __name__ == "__main__":
    u, v = map(int, input().split())
    find_shortest_array(u, v)
