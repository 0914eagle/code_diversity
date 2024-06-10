
def get_initial_state(n):
    state = list(map(int, input().split()))
    return state

def get_desired_state(state):
    min_num = 0
    for i in range(n):
        min_num = min_num * 10 + state[i]
    return min_num

def update_state(state):
    for i in range(n):
        state[i] = (state[i] + 1) % 10
    return state

def shift_state(state):
    temp = state[-1]
    for i in range(n-1):
        state[i] = state[i+1]
    state[-1] = temp
    return state

def main():
    n = int(input())
    state = get_initial_state(n)
    desired_state = get_desired_state(state)
    while desired_state != state:
        state = update_state(state)
        state = shift_state(state)
        desired_state = get_desired_state(state)
    print(desired_state)

if __name__ == '__main__':
    main()

