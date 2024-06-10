
def get_diverse_garland(s):
    n = len(s)
    dp = [[0] * 3 for _ in range(n)]
    for i in range(n):
        for j in range(3):
            if j == 0:
                dp[i][j] = dp[i - 1][1] + (1 if s[i - 1] == "B" else 0)
            elif j == 1:
                dp[i][j] = dp[i - 1][2] + (1 if s[i - 1] == "R" else 0)
            else:
                dp[i][j] = dp[i - 1][0] + (1 if s[i - 1] == "G" else 0)
    return dp[n - 1][:]

def solve(s):
    diverse_garland = get_diverse_garland(s)
    min_recolored = min(diverse_garland)
    recolored_positions = []
    for i in range(len(s)):
        if diverse_garland[i] == min_recolored:
            recolored_positions.append(i)
    return min_recolored, recolored_positions

def main():
    n = int(input())
    s = input()
    min_recolored, recolored_positions = solve(s)
    print(min_recolored)
    t = list(s)
    for i in recolored_positions:
        if s[i] == "R":
            t[i] = "G"
        elif s[i] == "G":
            t[i] = "B"
        else:
            t[i] = "R"
    print("".join(t))

if __name__ == '__main__':
    main()

