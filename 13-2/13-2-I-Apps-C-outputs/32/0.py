
def get_smallest_pack_size(bolts_needed, companies):
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

        # Check if the current company has enough bolts to sell
        if min_bolts_required[current_company] <= bolts_needed:
            # If the current company has enough bolts, return the minimum number of bolts required to buy a pack from this company
            return min_bolts_required[current_company]

        # If the current company does not have enough bolts, get the next company in the chain
        next_company = current_company + 1

        # Check if the next company is valid
        if next_company in companies:
            # If the next company is valid, add it to the queue
            queue.append(next_company)

    # If the queue is empty and no company has enough bolts, return impossible
    return "impossible"

def main():
    bolts_needed = int(input())
    companies = int(input())
    companies_info = []
    for i in range(companies):
        companies_info.append(list(map(int, input().split())))
    print(get_smallest_pack_size(bolts_needed, companies_info))

if __name__ == '__main__':
    main()

