
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the minimum number of bolts needed to buy a pack from each company
    min_bolts_needed = {}
    for company in companies:
        min_bolts_needed[company] = float('inf')

    # Initialize a queue to store the companies that need to be processed
    queue = []

    # Add the first company to the queue
    queue.append(companies[0])

    # Loop until the queue is empty
    while queue:
        # Get the current company from the queue
        current_company = queue.pop(0)

        # Check if the current company has enough bolts to sell
        if min_bolts_needed[current_company] <= bolts_needed:
            # If the current company has enough bolts, return the minimum number of bolts needed to buy a pack from this company
            return min_bolts_needed[current_company]

        # If the current company does not have enough bolts, get the next company in the chain
        next_company = current_company + 1

        # Check if the next company is valid
        if next_company < len(companies):
            # If the next company is valid, add it to the queue
            queue.append(next_company)

    # If the queue is empty and no company has enough bolts, return impossible
    return "impossible"

def main():
    # Read the input
    bolts_needed = int(input())
    companies = int(input())
    company_sizes = []
    for i in range(companies):
        company_sizes.append(list(map(int, input().split())))

    # Call the function to get the smallest pack
    smallest_pack = get_smallest_pack(bolts_needed, company_sizes)

    # Print the output
    print(smallest_pack)

if __name__ == '__main__':
    main()

