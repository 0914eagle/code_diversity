
def get_smallest_pack(B, k, companies):
    # Initialize the minimum advertised amount and the real amount
    min_advertised_amount = float('inf')
    min_real_amount = float('inf')
    
    # Loop through each company
    for i in range(k):
        # Get the advertised and real amounts for the current company
        advertised_amount, real_amount = get_company_info(companies[i])
        
        # If the real amount is greater than or equal to the target amount, update the minimum advertised amount and real amount
        if real_amount >= B:
            min_advertised_amount = min(min_advertised_amount, advertised_amount)
            min_real_amount = min(min_real_amount, real_amount)
    
    # If the minimum real amount is less than the target amount, it is not possible to find a pack with the target amount
    if min_real_amount < B:
        return "impossible"
    
    # Otherwise, return the minimum advertised amount
    return min_advertised_amount

def get_company_info(company):
    # Initialize the advertised and real amounts
    advertised_amount = 0
    real_amount = 0
    
    # Loop through each package size
    for package_size in company:
        # If the package size is greater than or equal to the target amount, update the real amount
        if package_size >= B:
            real_amount += package_size
        
        # Update the advertised amount
        advertised_amount += package_size
    
    # Return the advertised and real amounts
    return advertised_amount, real_amount

companies = [[40, 65], [100, 150], [300, 320]]
B = 310
k = 3
print(get_smallest_pack(B, k, companies))

