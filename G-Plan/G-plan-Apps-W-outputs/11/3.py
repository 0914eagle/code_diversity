
def find_max_xor_segment(n, arr):
    max_xor = 0
    current_xor = 0

    for num in arr:
        current_xor = max(current_xor ^ num, 0)
        max_xor = max(max_xor, current_xor)

    return max_xor

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_max_xor_segment(n, arr)
    print(result)
