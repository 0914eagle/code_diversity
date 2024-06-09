
def find_minimum_spanning_tree(points):
    # Sort the points based on their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set to store the connected components
    dsu = DisjointSet(points)

    # Initialize the minimum spanning tree weight to 0
    mst_weight = 0

    # Iterate through the sorted points
    for i in range(len(sorted_points)):
        # Get the current point and its x-coordinate
        current_point = sorted_points[i]
        current_x = current_point[0]

        # Find the nearest point to the current point in the other set
        nearest_point = dsu.find_nearest_point(current_point, sorted_points[i+1:])

        # If a nearest point is found, add the weight of the edge to the MST weight
        if nearest_point is not None:
            mst_weight += abs(current_point[0] - nearest_point[0]) + abs(current_point[1] - nearest_point[1])

            # Union the two points in the disjoint set
            dsu.union(current_point, nearest_point)

    return mst_weight

class DisjointSet:
    def __init__(self, points):
        self.parents = {point: point for point in points}
        self.ranks = {point: 0 for point in points}

    def find_nearest_point(self, point, points):
        nearest_point = None
        min_distance = float('inf')

        for other_point in points:
            distance = abs(point[0] - other_point[0]) + abs(point[1] - other_point[1])
            if distance < min_distance:
                min_distance = distance
                nearest_point = other_point

        return nearest_point

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

    def find(self, point):
        if self.parents[point] != point:
            self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

