
n, m = map(int, input().split())

if n > m:
    n, m = m, n

petya_points = n
vasya_points = 0

if n == 1:
    vasya_points = m - 1
else:
    vasya_points = m

print(petya_points, vasya_points)
