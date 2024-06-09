
def is_connected(S):
    # Initialize variables to keep track of the stations operated by each company
    company_a = 0
    company_b = 0
    
    # Iterate through the string S
    for i in range(len(S)):
        # If the current character is 'A', increment the count for Company A
        if S[i] == 'A':
            company_a += 1
        # If the current character is 'B', increment the count for Company B
        elif S[i] == 'B':
            company_b += 1
    
    # If there is at least one station operated by each company, return 'Yes'
    if company_a > 0 and company_b > 0:
        return 'Yes'
    # Otherwise, return 'No'
    else:
        return 'No'

if __name__ == '__main__':
    S = input()
    print(is_connected(S))

