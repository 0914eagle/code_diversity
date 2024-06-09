
def get_smallest_pack(bolts, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts = {}
    for company in companies:
        min_bolts[company] = float('inf')
    
    # Initialize a queue to store the companies that need to be processed
    queue = []
    
    # Add the manufacturer to the queue
    queue.append(companies[0])
    
    # Loop through the queue until it is empty
    while queue:
        # Get the current company from the queue
        current_company = queue.pop(0)
        
        # Loop through the companies that the current company buys from
        for previous_company in companies:
            # If the current company buys from the previous company, add the minimum number of bolts required to buy a pack from the previous company to the current company's minimum number of bolts
            if previous_company in companies[current_company]:
                min_bolts[current_company] += min_bolts[previous_company]
                
                # If the current company's minimum number of bolts is less than or equal to the number of bolts required, add the current company to the queue
                if min_bolts[current_company] <= bolts:
                    queue.append(current_company)
    
    # Return the smallest pack size that contains at least the number of bolts required
    return min(min_bolts, key=min_bolts.get)

def main():
    bolts, companies = map(int, input().split())
    company_sizes = [tuple(map(int, input().split())) for _ in range(companies)]
    print(get_smallest_pack(bolts, company_sizes))

if __name__ == '__main__':
    main()

