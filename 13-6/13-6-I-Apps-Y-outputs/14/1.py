
def get_max_sum_of_reposted_pictures(news_feed, k, x):
    n = len(news_feed)
    if n < x or n < k:
        return -1
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i >= k:
            dp[i] = max(dp[i - 1], dp[i - k] + news_feed[i - 1])
        else:
            dp[i] = dp[i - 1] + news_feed[i - 1]
    
    return dp[n]

