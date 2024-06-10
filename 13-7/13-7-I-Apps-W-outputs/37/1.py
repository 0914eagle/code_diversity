
def get_maximum_sum(a, edges):
    # Initialize a dictionary to store the pleasantness of each gift and the gifts that hang on it
    gifts = {}
    for i in range(len(a)):
        gifts[i + 1] = {
            "pleasantness": a[i],
            "hanging_on": set()
        }

    # Add the edges to the dictionary
    for u, v in edges:
        gifts[u]["hanging_on"].add(v)
        gifts[v]["hanging_on"].add(u)

    # Initialize the maximum sum of pleasantness to 0
    max_sum = 0

    # Iterate through the gifts and calculate the maximum sum of pleasantness that can be obtained by choosing them
    for gift in gifts:
        # If the gift has already been chosen, skip it
        if gift in gifts[gift]["hanging_on"]:
            continue

        # Initialize a set to store the gifts that have already been chosen
        chosen_gifts = set()

        # Initialize a queue to store the gifts that need to be processed
        queue = [gift]

        # Iterate through the queue and calculate the maximum sum of pleasantness that can be obtained by choosing them
        while queue:
            # Get the gift at the front of the queue
            current_gift = queue.pop(0)

            # If the gift has already been chosen, skip it
            if current_gift in chosen_gifts:
                continue

            # Add the gift to the set of chosen gifts
            chosen_gifts.add(current_gift)

            # Add the gifts that hang on the current gift to the queue
            queue += list(gifts[current_gift]["hanging_on"] - chosen_gifts)

        # Calculate the sum of pleasantness of the chosen gifts
        sum_of_pleasantness = sum(gifts[gift]["pleasantness"] for gift in chosen_gifts)

        # Update the maximum sum of pleasantness if necessary
        max_sum = max(max_sum, sum_of_pleasantness)

    return max_sum

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_sum(a, edges))

if __name__ == '__main__':
    main()

