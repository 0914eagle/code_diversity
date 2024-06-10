
def get_score(contest_rank):
    if contest_rank > 30:
        return 0
    else:
        return round(ranks[contest_rank])

def get_aggregate_score(contest_scores):
    return sum(sorted(contest_scores, reverse=True)[:4])

def get_final_rank(aggregate_scores):
    return 1 + aggregate_scores.index(max(aggregate_scores))

def get_worst_rank(n_contests, contest_scores):
    aggregate_scores = [get_aggregate_score(contest_scores[:i+1]) for i in range(n_contests)]
    return get_final_rank(aggregate_scores)

def main():
    n_contests, n_participants = map(int, input().split())
    contest_scores = []
    for _ in range(n_participants):
        contest_scores.append(list(map(int, input().split())))
    print(get_worst_rank(n_contests, contest_scores))

if __name__ == '__main__':
    main()

