
def minimum_spanning_tree(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set data structure to store the clusters
    dsu = DisjointSetUnion(points)

    # Initialize the total weight of the MST to 0
    total_weight = 0

    # Iterate through the points and form clusters
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Calculate the weight of the edge between the two points
            weight = manhattan_distance(sorted_points[i], sorted_points[j])

            # If the weight is less than or equal to the weight of the previously formed cluster, merge the two clusters
            if weight <= dsu.find_set(i).get_size() + dsu.find_set(j).get_size():
                dsu.union_sets(i, j)
                total_weight += weight

    return total_weight

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

class DisjointSetUnion:
    def __init__(self, points):
        self.parents = {i: i for i in range(len(points))}
        self.ranks = {i: 0 for i in range(len(points))}
        self.sizes = {i: 1 for i in range(len(points))}

    def find_set(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find_set(self.parents[i])
        return self.parents[i]

    def union_sets(self, i, j):
        i_root = self.find_set(i)
        j_root = self.find_set(j)

        if i_root == j_root:
            return

        if self.ranks[i_root] < self.ranks[j_root]:
            self.parents[i_root] = j_root
            self.sizes[j_root] += self.sizes[i_root]
        else:
            self.parents[j_root] = i_root
            self.sizes[i_root] += self.sizes[j_root]

            if self.ranks[i_root] == self.ranks[j_root]:
                self.ranks[i_root] += 1

