
def solve(S, queries):
    # Initialize a dictionary to store the count of AC as a substring
    ac_count = {}
    
    # Iterate through the string S
    for i in range(len(S)):
        # Check if the current substring starting at index i is AC
        if S[i:i+2] == "AC":
            # If it is, increment the count for this substring
            if i+2 in ac_count:
                ac_count[i+2] += 1
            else:
                ac_count[i+2] = 1
    
    # Initialize an empty list to store the answers
    answers = []
    
    # Iterate through the queries
    for l, r in queries:
        # Check if the current query is valid
        if l > r or l < 1 or r > len(S):
            answers.append(-1)
            continue
        
        # If the current query is valid, check if the count for the substring starting at index l and ending at index r is present in the dictionary
        if l in ac_count and r in ac_count:
            # If it is, add the count to the list of answers
            answers.append(ac_count[l] + ac_count[r])
        else:
            # If it is not, add 0 to the list of answers
            answers.append(0)
    
    return answers

