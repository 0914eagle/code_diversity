
n = int(input())
times = list(map(int, input().split()))
T = int(input())

times.sort()
max_students = 0

for i in range(n):
    count = 1
    for j in range(i+1, n):
        if times[j] - times[i] <= T:
            count += 1
    max_students = max(max_students, count)

print(max_students)
