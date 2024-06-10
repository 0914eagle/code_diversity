
def get_hamster_position(n):
    position = []
    for i in range(n):
        position.append(input())
    return position

def get_minimum_time(position):
    n = len(position)
    count = 0
    while position.count('X') != n//2:
        for i in range(n):
            if position[i] == 'x' and position[(i+1)%n] == 'X':
                position[i] = 'X'
                position[(i+1)%n] = 'x'
                count += 1
        if position.count('X') == n//2:
            break
    return count

def get_new_position(position):
    n = len(position)
    new_position = []
    for i in range(n):
        if position[i] == 'X':
            new_position.append('x')
        else:
            new_position.append('X')
    return ''.join(new_position)

if __name__ == '__main__':
    n = int(input())
    position = get_hamster_position(n)
    time = get_minimum_time(position)
    new_position = get_new_position(position)
    print(time)
    print(new_position)

