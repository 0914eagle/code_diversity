
n, m = map(int, input().split())

if n > m:
    n, m = m, n

petya_points = min(n, m)
vasya_points = n + m - 2 * petya_points

print(petya_points, vasya_points)
