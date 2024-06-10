
import itertools

def get_deck():
    deck = []
    for suit in itertools.product(range(4), repeat=2):
        for rank in range(1, 11):
            deck.append((rank, suit))
    return deck

def get_initial_state(deck, player1, player2):
    state = {}
    for i in range(10):
        state[player1] = {}
        state[player1][i] = deck[i]
        state[player2] = {}
        state[player2][i] = deck[i+10]
    return state

def get_next_state(state, player, card):
    next_state = {}
    for p in [player, 1-player]:
        next_state[p] = {}
        for i in range(10):
            if state[p][i] == card:
                next_state[p][i] = (None, None)
            else:
                next_state[p][i] = state[p][i]
    return next_state

def is_terminal_state(state):
    for p in [0, 1]:
        for i in range(10):
            if state[p][i][0] == None:
                return False
    return True

def evaluate(state):
    score = 0
    for p in [0, 1]:
        for i in range(10):
            if state[p][i][0] != None:
                score += 1
    return score

def minimax(state, depth, player):
    if depth == 0 or is_terminal_state(state):
        return evaluate(state)
    if player == 0:
        v = float('-inf')
        for card in state[player][0]:
            if card[0] != None:
                next_state = get_next_state(state, player, card)
                v = max(v, minimax(next_state, depth-1, 1-player))
        return v
    else:
        v = float('inf')
        for card in state[player][0]:
            if card[0] != None:
                next_state = get_next_state(state, player, card)
                v = min(v, minimax(next_state, depth-1, 1-player))
        return v

def solve(deck):
    player1 = 0
    player2 = 1
    state = get_initial_state(deck, player1, player2)
    depth = 10
    v = minimax(state, depth, player1)
    if v > 0:
        return "Theta wins"
    else:
        return "Theta loses"

if __name__ == '__main__':
    deck = list(input())
    print(solve(deck))

