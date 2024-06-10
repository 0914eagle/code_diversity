
def get_cafe_indices(n):
    return list(map(int, input().split()))

def get_last_visit(cafe_indices):
    last_visit = 0
    for i in range(1, len(cafe_indices)):
        if cafe_indices[i] > last_visit:
            last_visit = cafe_indices[i]
    return last_visit

def get_best_cafe(cafe_indices):
    best_cafe = 0
    for i in range(1, len(cafe_indices)):
        if cafe_indices[i] < cafe_indices[best_cafe]:
            best_cafe = i
    return best_cafe

def main():
    n = int(input())
    cafe_indices = get_cafe_indices(n)
    last_visit = get_last_visit(cafe_indices)
    best_cafe = get_best_cafe(cafe_indices)
    print(cafe_indices[best_cafe])

if __name__ == '__main__':
    main()

