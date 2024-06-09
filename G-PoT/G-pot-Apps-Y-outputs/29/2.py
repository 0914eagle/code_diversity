
N = int(input())
numbers = list(map(int, input().split()))

if len(numbers) == len(set(numbers)):
    print("YES")
else:
    print("NO")
