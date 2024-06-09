
def get_max_volume(n, cakes):
    # Sort the cakes by height in descending order
    cakes.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum volume and the current volume
    max_volume = 0
    current_volume = 0
    
    # Iterate through the cakes and calculate the volume of the current stack
    for i in range(n):
        current_volume += cakes[i][0] * cakes[i][1]
        max_volume = max(max_volume, current_volume)
    
    return max_volume

def main():
    n = int(input())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    print(get_max_volume(n, cakes))

if __name__ == '__main__':
    main()

