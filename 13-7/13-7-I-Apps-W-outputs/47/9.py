
def get_maximum_score(n, T, a, t):
    # Initialize the maximum score and the chosen problems to 0
    max_score = 0
    chosen_problems = []
    
    # Iterate over all possible subsets of problems
    for subset in range(2**n):
        # Convert the binary representation of the subset to a list of problem indices
        problems = [i for i in range(n) if subset & (1 << i)]
        
        # Check if the time required to solve the subset of problems is less than or equal to the length of the exam
        if sum(t[i] for i in problems) <= T:
            # Calculate the score for the current subset of problems
            score = 0
            for i in problems:
                score += a[i]
            
            # Update the maximum score and chosen problems if the current subset yields a higher score
            if score > max_score:
                max_score = score
                chosen_problems = problems
    
    return max_score, chosen_problems

def main():
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    
    max_score, chosen_problems = get_maximum_score(n, T, a, t)
    print(max_score)
    print(len(chosen_problems))
    print(*chosen_problems)

if __name__ == '__main__':
    main()

