
def read_input():
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    return n, r, w, h, gems

def get_maximum_gems(n, r, w, h, gems):
    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum number of gems collected to 0
    max_gems = 0
    
    # Iterate through the gems and check if they can be collected
    for gem in gems:
        x, y = gem
        # Check if the gem is within the reachable range
        if y <= h and x >= -r*y and x <= r*y:
            max_gems += 1
    
    return max_gems

def main():
    n, r, w, h, gems = read_input()
    print(get_maximum_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

