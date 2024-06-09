
def get_max_taste(fruits, k):
    max_taste = 0
    for i in range(len(fruits)):
        for j in range(i+1, len(fruits)):
            taste = fruits[i] + fruits[j]
            if taste % k == 0:
                max_taste = max(max_taste, taste)
    return max_taste

