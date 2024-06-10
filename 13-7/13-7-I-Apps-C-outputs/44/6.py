
def get_rating(rates):
    return sum(rates) / len(rates)

def get_matches(n, rates):
    matches = []
    for i in range(n):
        for j in range(i+1, n):
            matches.append([i, j])
    return matches

def get_match_results(matches, rates):
    results = []
    for match in matches:
        result = []
        for i in match:
            result.append(rates[i] - 1)
        results.append(result)
    return results

def get_optimized_rates(n, rates):
    matches = get_matches(n, rates)
    results = get_match_results(matches, rates)
    optimized_rates = rates[:]
    for result in results:
        for i in range(n):
            optimized_rates[i] = max(0, optimized_rates[i] - result[i])
    return optimized_rates

def get_match_strategy(n, rates):
    optimized_rates = get_optimized_rates(n, rates)
    final_rating = get_rating(optimized_rates)
    strategy = []
    for i in range(n):
        strategy.append([])
    for match in matches:
        for i in match:
            strategy[i].append(1)
        for i in range(n):
            if i not in match:
                strategy[i].append(0)
    return final_rating, strategy

def main():
    n = int(input())
    rates = list(map(int, input().split()))
    final_rating, strategy = get_match_strategy(n, rates)
    print(final_rating)
    print(len(strategy))
    for match in strategy:
        print("".join(map(str, match)))

if __name__ == '__main__':
    main()

