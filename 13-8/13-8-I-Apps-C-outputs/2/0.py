
def read_memory():
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(list(input()))
    return R, C, memory

def find_square_killers(memory):
    R, C, memory = read_memory()
    largest_killer_size = -1
    for i in range(R):
        for j in range(C):
            for k in range(1, min(R-i, C-j)):
                if memory[i+k][j+k] == memory[i][j] and memory[i+k][j] == memory[i][j+k]:
                    largest_killer_size = max(largest_killer_size, k)
    return largest_killer_size

def main():
    largest_killer_size = find_square_killers()
    print(largest_killer_size)

if __name__ == '__main__':
    main()

