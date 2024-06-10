
def get_tshirt_sizes():
    return list(map(int, input().split()))

def get_participants_sizes():
    return list(map(lambda x: x.split(','), input().splitlines()))

def can_allocate_tshirts(tshirt_sizes, participants_sizes):
    allocated_tshirts = [0] * 6
    for sizes in participants_sizes:
        if len(sizes) == 1:
            allocated_tshirts[sizes[0]] += 1
        else:
            allocated_tshirts[sizes[0]] += 1
            allocated_tshirts[sizes[1]] += 1
    
    for i in range(6):
        if allocated_tshirts[i] > tshirt_sizes[i]:
            return False
    
    return True

def allocate_tshirts(tshirt_sizes, participants_sizes):
    allocated_tshirts = [0] * 6
    for sizes in participants_sizes:
        if len(sizes) == 1:
            allocated_tshirts[sizes[0]] += 1
        else:
            allocated_tshirts[sizes[0]] += 1
            allocated_tshirts[sizes[1]] += 1
    
    solution = []
    for i in range(len(participants_sizes)):
        if allocated_tshirts[participants_sizes[i][0]] > 0:
            solution.append(participants_sizes[i][0])
            allocated_tshirts[participants_sizes[i][0]] -= 1
        else:
            solution.append(participants_sizes[i][1])
            allocated_tshirts[participants_sizes[i][1]] -= 1
    
    return solution

def main():
    tshirt_sizes = get_tshirt_sizes()
    participants_sizes = get_participants_sizes()
    
    if can_allocate_tshirts(tshirt_sizes, participants_sizes):
        print("YES")
        solution = allocate_tshirts(tshirt_sizes, participants_sizes)
        for size in solution:
            print(size)
    else:
        print("NO")

if __name__ == '__main__':
    main()

