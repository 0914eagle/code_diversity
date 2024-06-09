
def get_smallest_package(bolts_needed, companies):
    # Initialize a dictionary to store the number of bolts in each package
    package_bolts = {}
    # Loop through each company
    for company in companies:
        # Loop through each package type in the company
        for package in company:
            # If the package is not in the dictionary, add it and set the number of bolts to the advertised amount
            if package not in package_bolts:
                package_bolts[package] = package[1]
            # Otherwise, add the advertised amount to the current number of bolts in the package
            else:
                package_bolts[package] += package[1]
    
    # Loop through the packages and find the smallest package that contains at least the number of bolts needed
    for package in package_bolts:
        if package_bolts[package] >= bolts_needed:
            return package
    
    # If no package contains at least the number of bolts needed, return "impossible"
    return "impossible"

def main():
    bolts_needed = int(input())
    companies = []
    for i in range(int(input())):
        companies.append([int(j) for j in input().split()])
    print(get_smallest_package(bolts_needed, companies))

if __name__ == '__main__':
    main()

