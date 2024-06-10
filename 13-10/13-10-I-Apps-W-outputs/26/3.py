
def get_penalty(matrix_size, num_candies):
    
    penalty = 0
    # Implement your solution here
    return penalty

def get_paths(matrix_size, num_candies):
    
    paths = []
    # Implement your solution here
    return paths

if __name__ == '__main__':
    matrix_size = (int(input()), int(input()))
    num_candies = int(input())
    penalty = get_penalty(matrix_size, num_candies)
    paths = get_paths(matrix_size, num_candies)
    print(penalty)
    for path in paths:
        print(' '.join(map(str, path)))

