
def f1(n, string):
    # Find the longest alternating subsequence of the string
    longest_seq = 0
    for i in range(n):
        curr_seq = 1
        for j in range(i+1, n):
            if string[i] != string[j]:
                curr_seq += 1
            else:
                break
        longest_seq = max(longest_seq, curr_seq)
    return longest_seq

def f2(n, string):
    # Find the longest alternating subsequence of the string after flipping a single substring
    longest_seq = 0
    for i in range(n):
        for j in range(i+1, n):
            curr_seq = 1
            for k in range(j+1, n):
                if string[i] != string[k]:
                    curr_seq += 1
                else:
                    break
            longest_seq = max(longest_seq, curr_seq)
    return longest_seq

if __name__ == '__main__':
    n = int(input())
    string = input()
    print(f2(n, string))

