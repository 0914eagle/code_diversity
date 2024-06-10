
def get_min_energy(parts, ropes):
    # Initialize a dictionary to store the minimum energy to remove each part
    min_energy = {i: 0 for i in range(1, len(parts) + 1)}

    # Loop through each rope and update the minimum energy to remove each part
    for rope in ropes:
        x, y = rope
        min_energy[x] += parts[x - 1]
        min_energy[y] += parts[y - 1]

    # Return the minimum energy to remove all parts
    return sum(min_energy.values())

def main():
    # Read the number of parts and ropes
    n, m = map(int, input().split())

    # Read the parts and ropes
    parts = list(map(int, input().split()))
    ropes = [tuple(map(int, input().split())) for _ in range(m)]

    # Call the get_min_energy function and print the result
    print(get_min_energy(parts, ropes))

if __name__ == '__main__':
    main()

