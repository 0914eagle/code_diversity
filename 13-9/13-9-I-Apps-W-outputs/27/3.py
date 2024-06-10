
def check_line(line, k):
    # Initialize variables
    start_index = line.index("G")
    end_index = line.index("T")
    visited = set()
    queue = [(start_index, 0)]
    
    # Breadth-first search
    while queue:
        current_index, distance = queue.pop(0)
        if current_index == end_index:
            return True
        for i in range(max(current_index - k, 0), min(current_index + k + 1, len(line))):
            if line[i] == "." and i not in visited:
                queue.append((i, distance + 1))
                visited.add(i)
    
    return False

def main():
    n, k = map(int, input().split())
    line = input()
    print("YES") if check_line(line, k) else print("NO")

if __name__ == '__main__':
    main()

