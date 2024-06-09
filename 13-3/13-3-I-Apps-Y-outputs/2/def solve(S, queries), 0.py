
def solve(S, queries):
    # Initialize a dictionary to store the count of AC as a substring
    ac_count = {}
    
    # Iterate through the string S
    for i in range(len(S)):
        # Check if the current substring starting at index i is AC
        if S[i:i+2] == "AC":
            # If it is, increment the count by 1
            ac_count[i] = ac_count.get(i, 0) + 1
    
    # Initialize an empty list to store the answers
    answers = []
    
    # Iterate through the queries
    for l, r in queries:
        # Initialize a variable to store the count of AC as a substring in the current query
        count = 0
        
        # Iterate through the indices in the current query
        for i in range(l, r+1):
            # Check if the current index is in the dictionary of AC counts
            if i in ac_count:
                # If it is, increment the count by the value in the dictionary
                count += ac_count[i]
        
        # Add the count to the list of answers
        answers.append(count)
    
    return answers

