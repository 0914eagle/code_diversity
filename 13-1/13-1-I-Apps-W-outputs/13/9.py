
def f1(p, s, r):
    # Calculate the probability of Hasan scoring at least r goals
    prob_hasan_scores_r = comb(s-1, r-1) / comb(s-1, p-1)
    
    # Calculate the probability of Hasan scoring more than his opponents
    prob_hasan_scores_more = 0
    for i in range(r, s+1):
        prob_hasan_scores_more += comb(s-1, i-1) / comb(s-1, p-1)
    
    # Calculate the probability of Hasan winning
    prob_hasan_wins = prob_hasan_scores_r + prob_hasan_scores_more
    
    return prob_hasan_wins

def f2(p, s, r):
    # Calculate the probability of Hasan scoring at least r goals
    prob_hasan_scores_r = comb(s-1, r-1) / comb(s-1, p-1)
    
    # Calculate the probability of Hasan scoring more than his opponents
    prob_hasan_scores_more = 0
    for i in range(r, s+1):
        prob_hasan_scores_more += comb(s-1, i-1) / comb(s-1, p-1)
    
    # Calculate the probability of Hasan winning
    prob_hasan_wins = prob_hasan_scores_r + prob_hasan_scores_more
    
    return prob_hasan_wins

def main():
    p, s, r = map(int, input().split())
    print(f1(p, s, r))

if __name__ == '__main__':
    main()

