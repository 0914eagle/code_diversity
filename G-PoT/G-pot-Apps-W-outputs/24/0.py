
n, m = map(int, input().split())

if n > m:
    n, m = m, n

total_pairs = n + m - 1
petya_points = min(n, m)
vasya_points = total_pairs - petya_points

print(petya_points, vasya_points)
