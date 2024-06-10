
def find_smallest_string(n, k):
    if n < k or (n > 1 and k == 1):
        return "-1"

    result = ""
    for i in range(k):
        result += chr(ord('a') + i) * 2

    if len(result) < n:
        result += chr(ord('a') + k) * (n - len(result))

    return result

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(find_smallest_string(n, k))
