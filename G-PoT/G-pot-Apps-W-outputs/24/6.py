
n, m = map(int, input().split())

if n <= m:
    min_cubes = n
    max_cubes = m
else:
    min_cubes = m
    max_cubes = n

petya_points = min_cubes
vasya_points = min(min_cubes + 1, max_cubes)

print(petya_points, vasya_points)
