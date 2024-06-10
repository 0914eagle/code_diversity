
def get_rating(ratings):
    return sum(ratings) / len(ratings)

def get_optimal_strategy(n, ratings):
    optimal_strategy = []
    for i in range(n):
        optimal_strategy.append([0] * n)
    return optimal_strategy

def get_final_rating(n, ratings, strategy):
    final_rating = [0] * n
    for i in range(n):
        for j in range(n):
            if strategy[i][j] == 1:
                final_rating[j] -= 1
    return final_rating

def main():
    n = int(input())
    ratings = list(map(int, input().split()))
    optimal_strategy = get_optimal_strategy(n, ratings)
    final_rating = get_final_rating(n, ratings, optimal_strategy)
    print(get_rating(final_rating))
    print(len(optimal_strategy))
    for row in optimal_strategy:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()

