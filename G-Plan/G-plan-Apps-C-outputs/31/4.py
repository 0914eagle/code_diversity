t_sets(n, points):
    count_dict = {}
    for x, y in points:
        if y in count_dict:
            count_dict[y] += 1
        else:
            count_dict[y] = 1
    
    total_sets = 1
    for count in count_dict.values():
        total_sets *= count + 1
    
    return total_sets

if __name__ == "__main__":
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    
    result = count_sets(n, points)
    print(result)