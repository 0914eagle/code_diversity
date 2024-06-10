
def is_jacket_fastened_correctly(n, buttons):
    count_fastened = sum(buttons)
    if n == 1:
        return "YES" if count_fastened == 1 else "NO"
    return "YES" if count_fastened == n - 1 and buttons[-1] == 0 else "NO"

if __name__ == "__main__":
    n = int(input())
    buttons = list(map(int, input().split()))
    result = is_jacket_fastened_correctly(n, buttons)
    print(result)
