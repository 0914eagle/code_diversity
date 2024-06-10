
def longest_common_subsequence(strings):
    # Find the length of the longest common subsequence
    # of the first two strings
    lcs = 0
    for i in range(len(strings[0])):
        for j in range(len(strings[1])):
            if strings[0][i] == strings[1][j]:
                lcs += 1
                break
    # Compare the length of the longest common subsequence
    # of the first two strings with the length of the longest
    # common subsequence of the first string with the ith string
    # for all i in range(2, len(strings)):
    for i in range(2, len(strings)):
        curr_lcs = 0
        for j in range(len(strings[0])):
            for k in range(len(strings[i])):
                if strings[0][j] == strings[i][k]:
                    curr_lcs += 1
                    break
        if curr_lcs > lcs:
            lcs = curr_lcs
    return lcs

def main():
    # Read the input data
    n, k = map(int, input().split())
    strings = []
    for i in range(n):
        strings.append(input())
    # Find the longest common subsequence of all strings
    lcs = longest_common_subsequence(strings)
    # Print the result
    print(lcs)

if __name__ == '__main__':
    main()

