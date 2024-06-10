
def main():
    n = int(input())
    ans = []
    for i in range(n):
        ans.append(expected_value(i))
    print(*ans, sep='\n')

def expected_value(s):
    # Initialize the probability of each board
    prob = [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
    # Initialize the number of black stones for each board
    num_black = [0, 1, 0, 2, 1, 3, 2, 3]
    # Loop through each board and calculate the expected number of black stones
    for i in range(8):
        prob[i] *= num_black[i]
    # Calculate the expected value modulo 998244353
    expected = 0
    for i in range(8):
        expected += prob[i] * num_black[i]
    expected = expected % 998244353
    return expected

if __name__ == '__main__':
    main()

