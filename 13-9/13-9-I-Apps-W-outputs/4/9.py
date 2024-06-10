
def get_next_number(number):
    number = str(number)
    number = number[1:] + number[0]
    number = int(number)
    return number

def get_smallest_number(n, initial_state):
    current_state = initial_state
    while True:
        current_state = get_next_number(current_state)
        if len(str(current_state)) == n:
            break
    return current_state

if __name__ == '__main__':
    n = int(input())
    initial_state = int(input())
    print(get_smallest_number(n, initial_state))

