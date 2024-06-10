
def get_number_of_points_in_area(x, y, l, r, a):
    
    return len([(x_i, y_i) for x_i, y_i in zip(x, y) if l < x_i < r and y_i > a])

def get_all_sets_of_points(x, y, l, r, a):
    
    points_in_area = get_number_of_points_in_area(x, y, l, r, a)
    all_sets = []
    for i in range(points_in_area):
        for j in range(i+1, points_in_area):
            all_sets.append([(x[i], y[i]), (x[j], y[j])])
    return all_sets

def get_number_of_different_sets(x, y, l, r, a):
    
    all_sets = get_all_sets_of_points(x, y, l, r, a)
    return len(set(map(tuple, all_sets)))

if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    l, r, a = map(int, input().split())
    print(get_number_of_different_sets(x, y, l, r, a))

