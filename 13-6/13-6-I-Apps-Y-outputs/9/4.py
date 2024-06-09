
def sort_tickets(arr):
    return sorted(arr)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*sort_tickets(arr))

if __name__ == '__main__':
    main()

