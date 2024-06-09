
def count_suitable_colorings(n, k):
    def count_beautiful_colorings(n):
        if n == 1:
            return 2
        else:
            return (count_beautiful_colorings(n-1) * 2) % 998244353
    
    def count_suitable_colorings_helper(n, k, curr_row, curr_col, color, dp):
        if curr_row == n:
            return 1
        
        if (curr_row, curr_col, color) in dp:
            return dp[(curr_row, curr_col, color)]
        
        count = 0
        for i in range(2):
            for j in range(2):
                if i == j and curr_col == 0:
                    continue
                if abs(i - j) == abs(curr_col - color):
                    continue
                count += count_suitable_colorings_helper(n, k, curr_row+1, (curr_col+1)%n, i, dp)
        
        dp[(curr_row, curr_col, color)] = count
        return count
    
    dp = {}
    return count_suitable_colorings_helper(n, k, 0, 0, 0, dp)

def main():
    n, k = map(int, input().split())
    print(count_suitable_colorings(n, k) % 998244353)

if __name__ == '__main__':
    main()

