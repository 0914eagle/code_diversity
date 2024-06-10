
def roll_die(n, k):
    # Base case: if we are allowed to roll only once, return the score of the single roll
    if k == 1:
        return sum(die(n))
    
    # Recursive case: roll the die and recurse with the updated number of rolls and score
    score = 0
    for _ in range(k):
        score += sum(die(n))
    return score

def expected_score(n, k):
    # Calculate the expected score by summing the probability of each outcome and multiplying by the score of that outcome
    expected = 0
    for i in range(1, n+1):
        expected += (i / n) * roll_die(n, k-1)
    return expected

def main():
    n, k = map(int, input().split())
    print(expected_score(n, k))

if __name__ == '__main__':
    main()

