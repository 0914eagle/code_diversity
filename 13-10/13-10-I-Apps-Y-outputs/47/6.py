
import sys

def optimal_order(passwords):
    # Sort the passwords in descending order of probability
    passwords.sort(key=lambda x: x[1], reverse=True)
    # Calculate the cumulative sum of the probabilities
    cum_sum = [0]
    for i in range(1, len(passwords)):
        cum_sum.append(cum_sum[i-1] + passwords[i][1])
    # Find the index of the first password with probability greater than 1/2
    mid = 0
    while cum_sum[mid] < 0.5:
        mid += 1
    # Calculate the expected number of attempts
    expected_attempts = 0
    for i in range(mid):
        expected_attempts += passwords[i][1] / (1 - cum_sum[i])
    for i in range(mid, len(passwords)):
        expected_attempts += passwords[i][1] / cum_sum[i]
    return expected_attempts

def main():
    num_passwords = int(input())
    passwords = []
    for _ in range(num_passwords):
        password, prob = input().split()
        passwords.append((password, float(prob)))
    print(optimal_order(passwords))

if __name__ == '__main__':
    main()

