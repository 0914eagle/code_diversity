
def get_cafe_index(cafes, last_visit):
    # Find the cafe with the last visit time that is before the last visit times of all other cafes
    for i in range(len(cafes)):
        if last_visit[i] < last_visit[i-1]:
            return i
    return -1

def main():
    n = int(input())
    cafes = list(map(int, input().split()))
    last_visit = [0] * n
    for i in range(n):
        last_visit[cafes[i]-1] = i+1
    cafe_index = get_cafe_index(cafes, last_visit)
    print(cafes[cafe_index])

if __name__ == '__main__':
    main()

