
def get_aggregate_score(scores):
    return sum(sorted(scores, reverse=True)[:4])

def get_rank(aggregate_score, num_contests):
    return num_contests - aggregate_score + 1

def get_worst_rank(scores, num_contests):
    aggregate_score = get_aggregate_score(scores)
    return get_rank(aggregate_score, num_contests)

def main():
    num_contests, num_contestants = map(int, input().split())
    scores = []
    for _ in range(num_contestants):
        scores.append(list(map(int, input().split())))
    print(get_worst_rank(scores, num_contests))

if __name__ == '__main__':
    main()

