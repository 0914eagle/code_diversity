
from itertools import combinations
from sympy import primefactors

def calculate_revenue(data_pieces, special_properties):
    dp = [[0] * (1 << len(data_pieces)) for _ in range(len(data_pieces) + 1)]

    for i in range(1, len(data_pieces) + 1):
        for mask in range(1, 1 << len(data_pieces)):
            for j in range(len(data_pieces)):
                if mask & (1 << j):
                    dp[i][mask] = max(dp[i][mask], dp[i - 1][mask ^ (1 << j)] + len(set(primefactors(sum(special_properties[k] for k in range(j + 1)))))

    return dp[len(data_pieces)][(1 << len(data_pieces)) - 1]

if __name__ == "__main__":
    N = int(input())
    special_properties = list(map(int, input().split()))
    revenue = calculate_revenue(range(1, N + 1), special_properties)
    print(revenue)
