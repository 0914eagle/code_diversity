
def get_optimal_position(n, position):
    # Calculate the number of standing hamsters
    num_standing = position.count('X')
    
    # Calculate the number of minutes needed
    if num_standing == n / 2:
        return 0
    else:
        return 1

def get_new_position(n, position):
    # Calculate the number of standing hamsters
    num_standing = position.count('X')
    
    # Calculate the number of minutes needed
    if num_standing == n / 2:
        return position
    else:
        # Flip the standing hamsters to sitting hamsters
        new_position = []
        for i in range(n):
            if position[i] == 'X':
                new_position.append('x')
            else:
                new_position.append('X')
        return ''.join(new_position)

if __name__ == '__main__':
    n = int(input())
    position = input()
    print(get_optimal_position(n, position))
    print(get_new_position(n, position))

