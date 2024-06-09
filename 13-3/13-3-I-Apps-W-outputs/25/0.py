
def find_rearrangement(arr):
    n = len(arr)
    sum_arr = sum(arr)
    if sum_arr == 0:
        return "NO"
    for i in range(n):
        curr_sum = sum(arr[:i+1])
        if curr_sum == 0:
            return "NO"
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(find_rearrangement(arr))

if __name__ == '__main__':
    main()

