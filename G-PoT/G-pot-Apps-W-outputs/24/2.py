
n, m = map(int, input().split())

if n > m:
    n, m = m, n

petya_points = n
vasya_points = min(n, m - 1)

print(petya_points, vasya_points)
