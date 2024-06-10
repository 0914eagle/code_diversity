
def get_max_pleasantness(a, edges):
    # Initialize a dictionary to store the pleasantness of each gift and the gifts that hang on it
    pleasantness = {i: a[i-1] for i in range(1, len(a)+1)}
    hanging_on = {i: set() for i in range(1, len(a)+1)}

    # Populate the dictionary with the edges of the tree
    for u, v in edges:
        hanging_on[u].add(v)
        hanging_on[v].add(u)

    # Initialize a set to store the gifts that Vladik and Chloe have chosen
    chosen = set()

    # Function to recursively find the maximum pleasantness sum
    def find_max_pleasantness(current_gift, current_sum):
        nonlocal chosen

        # If the current gift has already been chosen, return the current sum
        if current_gift in chosen:
            return current_sum

        # If the current gift has not been chosen, add its pleasantness to the current sum
        chosen.add(current_gift)
        current_sum += pleasantness[current_gift]

        # Recursively call the function for each gift that hangs on the current gift
        for next_gift in hanging_on[current_gift]:
            current_sum = find_max_pleasantness(next_gift, current_sum)

        return current_sum

    # Call the function for the first gift (which is gift 1)
    max_pleasantness = find_max_pleasantness(1, 0)

    # If the maximum pleasantness is positive, return it
    if max_pleasantness > 0:
        return max_pleasantness

    # If the maximum pleasantness is 0 or negative, return "Impossible"
    return "Impossible"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_max_pleasantness(a, edges))

if __name__ == '__main__':
    main()

