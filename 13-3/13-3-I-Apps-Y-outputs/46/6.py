
def get_triangle_count(sticks):
    count = 0
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if sticks[i] + sticks[j] > sticks[k] and sticks[i] + sticks[k] > sticks[j] and sticks[j] + sticks[k] > sticks[i]:
                    count += 1
    return count

sticks = list(map(int, input().split()))
print(get_triangle_count(sticks))

