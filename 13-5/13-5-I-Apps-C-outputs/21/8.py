
def get_smallest_pack(bolts, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts_required = {}
    for company in companies:
        min_bolts_required[company] = float('inf')

    # Initialize a queue to store the companies that need to be visited
    queue = []

    # Add the first company to the queue
    queue.append(companies[0])

    # Loop until the queue is empty
    while queue:
        # Get the current company from the queue
        current_company = queue.pop(0)

        # Check if the current company can provide the required number of bolts
        if min_bolts_required[current_company] <= bolts:
            # If the current company can provide the required number of bolts, return the pack size
            return min_bolts_required[current_company]

        # If the current company cannot provide the required number of bolts, add its neighbors to the queue
        for neighbor in companies[current_company]:
            queue.append(neighbor)

    # If the queue is empty and no pack size has been found, return -1
    return -1

def main():
    # Read the input
    bolts, companies = map(int, input().split())
    company_sizes = [list(map(int, input().split())) for _ in range(companies)]

    # Get the smallest pack size
    smallest_pack = get_smallest_pack(bolts, company_sizes)

    # Print the result
    print(smallest_pack)

if __name__ == '__main__':
    main()

