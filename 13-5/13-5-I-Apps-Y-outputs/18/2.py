
def get_image_size(image):
    return len(image), len(image[0])

def get_island_count(image):
    island_count = 0
    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col] == "L":
                island_count += 1
    return island_count

def f1(...):
    # Your code here
    pass

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    image = []
    for _ in range(int(input())):
        image.append(input())
    print(get_island_count(image))

