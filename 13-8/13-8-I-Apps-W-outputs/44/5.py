
def get_min_energy(n, m, v, edges):
    # Initialize a dictionary to store the minimum energy to remove each part
    min_energy = {i: v[i-1] for i in range(1, n+1)}
    # Loop through all the edges
    for i, j in edges:
        # If the energy to remove part i is greater than the energy to remove part j plus the energy to remove part i, update the minimum energy to remove part i
        if min_energy[i] > min_energy[j] + v[i-1]:
            min_energy[i] = min_energy[j] + v[i-1]
    # Return the minimum energy to remove all parts
    return sum(min_energy.values())

def main():
    # Read the input data
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    # Call the get_min_energy function and print the result
    print(get_min_energy(n, m, v, edges))

if __name__ == '__main__':
    main()

