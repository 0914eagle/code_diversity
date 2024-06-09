
def get_max_distance(N, T, s, a):
    # Calculate the minimum radians needed to go from angle a to b
    def dist(a, b):
        return min(abs(a - b), abs(a - b + 2 * math.pi), abs(a - b - 2 * math.pi))

    # Initialize the maximum distance
    max_dist = 0

    # Iterate over each star
    for i in range(N):
        # Calculate the distance that the spaceship can travel from star i
        dist_i = max(0, T[i] - s[i] * dist(a[i], math.pi / 2))

        # Update the maximum distance
        max_dist += dist_i

    return max_dist

def main():
    # Read the input
    N = int(input())
    T = []
    s = []
    a = []
    for i in range(N):
        T.append(float(input()))
        s.append(float(input()))
        a.append(float(input()))

    # Calculate the maximum distance
    max_dist = get_max_distance(N, T, s, a)

    # Print the result
    print(max_dist)

if __name__ == '__main__':
    main()

