
def solve(s, b):
    n = len(s)
    m = len(b)
    if n == m:
        return s
    
    # initialize a dictionary to store the number of letters that are later in the alphabet
    later_letters = {}
    for i in range(n):
        later_letters[s[i]] = 0
    
    # iterate through the string and count the number of letters that are later in the alphabet
    for i in range(n):
        for j in range(i+1, n):
            if s[j] > s[i]:
                later_letters[s[i]] += 1
    
    # initialize an array to store the distances from the current index to the indices with later letters
    distances = [0] * n
    for i in range(n):
        distances[i] = later_letters[s[i]]
    
    # sort the array in descending order
    distances.sort(reverse=True)
    
    # create a new string with the same length as the input string
    t = [""] * n
    
    # iterate through the input string and assign the letters to the new string
    for i in range(n):
        t[i] = s[distances[i] - 1]
    
    return "".join(t)

