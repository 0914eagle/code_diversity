
def get_smallest_pack_size(bolts_needed, companies):
    # Initialize a dictionary to store the minimum advertised amount and real amount of bolts for each company
    company_info = {}
    for company in companies:
        company_info[company] = {}
        company_info[company]["min_advertised_amount"] = float("inf")
        company_info[company]["real_amount"] = 0
    
    # Loop through the companies and calculate the minimum advertised amount and real amount of bolts for each company
    for company in companies:
        for package in companies[company]:
            company_info[company]["min_advertised_amount"] = min(company_info[company]["min_advertised_amount"], package)
            company_info[company]["real_amount"] += package
    
    # Find the company with the smallest advertised amount that contains at least the number of bolts needed
    for company in companies:
        if company_info[company]["min_advertised_amount"] <= bolts_needed:
            return company_info[company]["min_advertised_amount"]
    
    # If no company has a package with the number of bolts needed, return "impossible"
    return "impossible"

