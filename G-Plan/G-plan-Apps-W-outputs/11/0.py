
def find_max_xor_segment(n, arr):
    max_xor = 0
    current_xor = 0

    for num in arr:
        current_xor = max(num, current_xor ^ num)
        max_xor = max(max_xor, current_xor)

    return max_xor

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_max_xor_segment(n, arr))
