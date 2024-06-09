
N = int(input())
sequence = list(map(int, input().split()))

if len(set(sequence)) == N:
    print("YES")
else:
    print("NO")
