
def get_largest_square_killer(memory):
    rows, cols = len(memory), len(memory[0])
    largest_killer = 0
    
    for row in range(rows):
        for col in range(cols):
            if memory[row][col] == "1":
                current_killer = 1
                for i in range(row, rows):
                    for j in range(col, cols):
                        if memory[i][j] == "0":
                            break
                        current_killer += 1
                    else:
                        continue
                    break
                largest_killer = max(largest_killer, current_killer)
    
    return largest_killer

def main():
    rows, cols = map(int, input().split())
    memory = [input() for _ in range(rows)]
    largest_square_killer = get_largest_square_killer(memory)
    print(largest_square_killer)

if __name__ == '__main__':
    main()

