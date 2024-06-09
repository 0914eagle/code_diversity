
n = int(input())
times = list(map(int, input().split()))
T = int(input())

times.sort()
max_students = 1

for i in range(n):
    for j in range(i+1, n):
        if times[j] - times[i] <= T:
            max_students = max(max_students, j - i + 1)

print(max_students)
