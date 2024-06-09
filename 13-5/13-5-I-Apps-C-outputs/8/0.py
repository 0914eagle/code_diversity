
def f1(n, string):
    # find the longest alternating subsequence in the given string
    longest_alternating_subsequence = 0
    for i in range(len(string)):
        current_subsequence = ""
        for j in range(i, len(string)):
            if string[j] == "0":
                current_subsequence += "1"
            else:
                current_subsequence += "0"
            if len(current_subsequence) > longest_alternating_subsequence:
                longest_alternating_subsequence = len(current_subsequence)
    return longest_alternating_subsequence

def f2(n, string):
    # find the longest alternating subsequence in the given string after flipping a substring
    longest_alternating_subsequence = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            flipped_substring = ""
            for char in substring:
                if char == "0":
                    flipped_substring += "1"
                else:
                    flipped_substring += "0"
            current_subsequence = flipped_substring
            for k in range(j, len(string)):
                if string[k] == "0":
                    current_subsequence += "1"
                else:
                    current_subsequence += "0"
            if len(current_subsequence) > longest_alternating_subsequence:
                longest_alternating_subsequence = len(current_subsequence)
    return longest_alternating_subsequence

if __name__ == '__main__':
    n = int(input())
    string = input()
    print(f2(n, string))

