
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts_required = {}
    for company in companies:
        min_bolts_required[company] = float('inf')

    # Initialize a queue to store the companies that need to be processed
    queue = []

    # Add the first company to the queue
    queue.append(companies[0])

    # Loop until the queue is empty
    while queue:
        # Get the current company from the queue
        current_company = queue.pop(0)

        # Check if the current company can provide the required number of bolts
        if min_bolts_required[current_company] <= bolts_needed:
            # If the current company can provide the required number of bolts, return the pack size
            return min_bolts_required[current_company]

        # If the current company cannot provide the required number of bolts, find the next company in the chain
        for next_company in companies:
            # Check if the next company is not the current company and if it has a pack size that is greater than the current company's pack size
            if next_company != current_company and next_company not in min_bolts_required:
                # Add the next company to the queue
                queue.append(next_company)

                # Set the minimum number of bolts required to buy a pack from the next company to the current company's pack size
                min_bolts_required[next_company] = min_bolts_required[current_company]

    # If the queue is empty and the required number of bolts cannot be provided, return impossible
    return "impossible"

def main():
    # Read the input
    bolts_needed = int(input())
    companies = int(input())
    company_data = []
    for _ in range(companies):
        company_data.append(list(map(int, input().split())))

    # Call the get_smallest_pack function and print the result
    print(get_smallest_pack(bolts_needed, company_data))

if __name__ == '__main__':
    main()

