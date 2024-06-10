
def get_strengths(n, k, x, strengths):
    # Sort the strengths in increasing order
    sorted_strengths = sorted(strengths)

    # Perform the operation k times
    for i in range(k):
        # Take the bitwise XOR of each alternate strength with x and update it
        for j in range(0, n, 2):
            sorted_strengths[j] = sorted_strengths[j] ^ x

    return sorted_strengths

def get_min_max_strengths(n, k, x, strengths):
    sorted_strengths = get_strengths(n, k, x, strengths)
    return (sorted_strengths[0], sorted_strengths[-1])

if __name__ == '__main__':
    n, k, x = map(int, input().split())
    strengths = list(map(int, input().split()))
    print(*get_min_max_strengths(n, k, x, strengths))

