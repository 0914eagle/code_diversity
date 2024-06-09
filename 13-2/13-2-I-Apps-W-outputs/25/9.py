
n = int(input())
cities = list(map(int, input().split()))

# Calculate the distance between each pair of cities
distances = []
for i in range(n):
    for j in range(i+1, n):
        distance = abs(cities[i] - cities[j])
        distances.append(distance)

# Find the minimum distance and the number of pairs with that distance
min_distance = min(distances)
num_pairs = len([distance for distance in distances if distance == min_distance])

print(min_distance, num_pairs)

