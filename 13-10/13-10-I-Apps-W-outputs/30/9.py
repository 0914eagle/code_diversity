
def count_violas(violas, k):
    return len([viola for viola in violas if viola[1] >= k])

def count_pictures(r, c, n, k):
    violas = []
    for _ in range(n):
        x, y = map(int, input().split())
        violas.append([x, y])
    
    violas.sort(key=lambda x: x[0])
    
    pictures = 0
    for i in range(r):
        for j in range(c):
            if count_violas(violas, k) > 0:
                pictures += 1
    
    return pictures

if __name__ == '__main__':
    r, c, n, k = map(int, input().split())
    print(count_pictures(r, c, n, k))

