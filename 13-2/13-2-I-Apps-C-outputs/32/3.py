
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the minimum number of bolts needed to buy a pack from each company
    min_bolts_needed = {}
    for company in companies:
        min_bolts_needed[company] = float('inf')

    # Initialize a set to store the companies that have been visited
    visited_companies = set()

    # Start the search from the first company
    current_company = companies[0]
    current_bolts_needed = bolts_needed

    while current_company not in visited_companies:
        # Mark the current company as visited
        visited_companies.add(current_company)

        # Get the minimum number of bolts needed to buy a pack from the current company
        min_bolts_needed_current_company = min_bolts_needed[current_company]

        # If the current company has enough bolts to sell, return the current pack
        if current_bolts_needed <= min_bolts_needed_current_company:
            return current_bolts_needed

        # If the current company does not have enough bolts to sell, find the next company in the chain
        next_company = get_next_company(current_company, companies)

        # If there is no next company, return impossible
        if next_company is None:
            return "impossible"

        # Update the current bolts needed and the current company
        current_bolts_needed = current_bolts_needed - min_bolts_needed_current_company
        current_company = next_company

    # If the loop completes, return the smallest pack size that can be bought
    return min_bolts_needed[current_company]

def get_next_company(current_company, companies):
    # Find the next company in the chain
    for company in companies:
        if company != current_company and company not in visited_companies:
            return company
    return None

if __name__ == '__main__':
    bolts_needed = int(input())
    companies = int(input())
    companies_info = []
    for i in range(companies):
        companies_info.append(list(map(int, input().split())))
    print(get_smallest_pack(bolts_needed, companies_info))

