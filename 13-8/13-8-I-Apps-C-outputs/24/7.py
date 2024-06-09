
def get_minimum_spanning_tree_weight(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Create a disjoint set to store the clusters
    dset = DisjointSet(points)

    # Initialize the total weight of the MST to 0
    total_weight = 0

    # Iterate through the points and form clusters
    for i in range(len(sorted_points)):
        # Get the current point and its cluster
        current_point = sorted_points[i]
        current_cluster = dset.find(current_point)

        # Find the nearest neighbor of the current point that is not in the same cluster
        nearest_neighbor = None
        nearest_neighbor_distance = float('inf')
        for j in range(i+1, len(sorted_points)):
            neighbor = sorted_points[j]
            if dset.find(neighbor) != current_cluster:
                distance = manhattan_distance(current_point, neighbor)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor = neighbor
                    nearest_neighbor_distance = distance

        # If a nearest neighbor is found, add the weight of the edge to the total weight and merge the clusters
        if nearest_neighbor is not None:
            total_weight += nearest_neighbor_distance
            dset.union(current_point, nearest_neighbor)

    return total_weight

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

class DisjointSet:
    def __init__(self, points):
        self.parents = {point: point for point in points}
        self.ranks = {point: 0 for point in points}

    def find(self, point):
        if self.parents[point] != point:
            self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

    def union(self, point1, point2):
        root1 = self.find(point1)
        root2 = self.find(point2)
        if root1 != root2:
            if self.ranks[root1] > self.ranks[root2]:
                self.parents[root2] = root1
            elif self.ranks[root1] < self.ranks[root2]:
                self.parents[root1] = root2
            else:
                self.parents[root2] = root1
                self.ranks[root1] += 1

