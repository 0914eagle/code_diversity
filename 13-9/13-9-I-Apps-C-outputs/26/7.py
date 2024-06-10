
def get_number_of_crosses(n, portals):
    # Initialize a list to store the number of crosses in each room
    num_crosses = [0] * (n + 1)
    num_crosses[1] = 1

    # Iterate through each room and update the number of crosses
    for i in range(1, n):
        if num_crosses[i] % 2 == 0:
            num_crosses[i + 1] += 1
        else:
            num_crosses[portals[i - 1]] += 1

    return num_crosses[n]

def get_number_of_portals(n, portals):
    # Initialize a set to store the visited rooms
    visited = set()
    visited.add(1)

    # Iterate through each room and check if it has been visited before
    for i in range(1, n):
        if portals[i - 1] not in visited:
            visited.add(portals[i - 1])
        else:
            return i

    return n

def solve(n, portals):
    num_crosses = get_number_of_crosses(n, portals)
    num_portals = get_number_of_portals(n, portals)
    return (num_crosses * num_portals) % 1000000007

if __name__ == '__main__':
    n = int(input())
    portals = [int(x) for x in input().split()]
    print(solve(n, portals))

