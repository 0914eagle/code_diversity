
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop through each letter of the Latin alphabet
    for i in range(0, 26):
        # If the current letter has not been used yet, add it to the result string
        if freq[i] == 0:
            result += chr(i + ord('a'))
            # Increment the frequency of the current letter
            freq[i] += 1
        # If the current letter has already been used, find the next available letter
        else:
            for j in range(i + 1, 26):
                if freq[j] == 0:
                    result += chr(j + ord('a'))
                    freq[j] += 1
                    break
    # If the result string is not long enough, add additional letters to make it length n
    while len(result) < n:
        for i in range(0, 26):
            if freq[i] == 0:
                result += chr(i + ord('a'))
                freq[i] += 1
                break
    return result

def f1(n, k):
    
    # Construct a string that maximizes the minimal frequency of any letter
    result = get_maximal_string(n, k)
    # If the result string is not long enough, add additional letters to make it length n
    while len(result) < n:
        result += "a"
    return result

def f2(...):
    
    # Construct a string that maximizes the minimal frequency of any letter
    result = get_maximal_string(n, k)
    # If the result string is not long enough, add additional letters to make it length n
    while len(result) < n:
        result += "a"
    return result

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(f1(n, k))
        print(f2(n, k))

