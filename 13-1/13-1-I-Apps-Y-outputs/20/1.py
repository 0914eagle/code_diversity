
def get_maximum_necklace_length(n, k, s):
    # Your code here
    return len(s)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        print(get_maximum_necklace_length(n, k, s))

