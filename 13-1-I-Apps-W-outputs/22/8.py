
def get_max_taste(fruits, k):
    max_taste = -1
    for i in range(len(fruits)):
        for j in range(i+1, len(fruits)):
            taste = fruits[i] + fruits[j]
            calories = fruits[i][1] + fruits[j][1]
            if taste / calories == k:
                max_taste = max(max_taste, taste)
    return max_taste

