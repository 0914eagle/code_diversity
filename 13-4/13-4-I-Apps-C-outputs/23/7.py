
def can_zax_and_xaz_coexist(m, n, resources):
    # Initialize a set to store the unique resources
    unique_resources = set()

    # Iterate over the resources on each island
    for island in resources:
        # Add the resources to the set
        unique_resources.update(island)

    # Check if the set has all the resources
    return len(unique_resources) == n


if __name__ == "__main__":
    m, n = map(int, input().split())
    resources = []
    for _ in range(m):
        resources.append(set(map(int, input().split())))

    print("YES") if can_zax_and_xaz_coexist(m, n, resources) else print("NO")

