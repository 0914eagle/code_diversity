
def get_correct_bracket_sequences(n):
    if n == 1:
        return 1
    else:
        return 2 * get_correct_bracket_sequences(n - 1)

def get_maximum_matching(n):
    correct_bracket_sequences = get_correct_bracket_sequences(n)
    return correct_bracket_sequences * (correct_bracket_sequences - 1) // 2

if __name__ == '__main__':
    n = int(input())
    print(get_maximum_matching(n) % (10**9 + 7))

