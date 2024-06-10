
def get_initial_state(S):
    
    N = len(S)
    state = [0] * N
    for i in range(N):
        if S[i] == "L":
            state[i] += 1
    return state

def get_final_state(state, moves):
    
    N = len(state)
    for _ in range(moves):
        new_state = [0] * N
        for i in range(N):
            if state[i] > 0:
                new_state[(i+1)%N] += state[i]
        state = new_state
    return state

def main():
    S = input()
    state = get_initial_state(S)
    moves = 10**100
    final_state = get_final_state(state, moves)
    print(*final_state)

if __name__ == '__main__':
    main()

