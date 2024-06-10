
def solve(S):
    N = len(S)
    left_count = 1
    right_count = 1
    for i in range(N-2):
        if S[i] == 'L':
            left_count += 1
        else:
            right_count += 1
    return [left_count, right_count]

def main():
    S = input()
    print(solve(S))

if __name__ == '__main__':
    main()

