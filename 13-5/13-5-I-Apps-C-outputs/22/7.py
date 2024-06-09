
def read_input():
    n, p = map(int, input().split())
    t = list(map(int, input().split()))
    s = []
    e = []
    for i in range(p):
        s_i, e_i = map(int, input().split())
        s.append(s_i)
        e.append(e_i)
    return n, p, t, s, e

def find_max_score(n, p, t, s, e):
    # Initialize the maximum score and the current score
    max_score = 0
    curr_score = 0
    
    # Initialize the SP meter and the current SP phrase
    sp_meter = 0
    curr_sp_phrase = 0
    
    # Iterate through the notes and update the score and SP meter
    for i in range(n):
        # If the current note is within the current SP phrase, update the SP meter
        if s[curr_sp_phrase] <= t[i] <= e[curr_sp_phrase]:
            sp_meter += 1
        
        # If the current note is the first note of the current SP phrase, update the SP meter and the current SP phrase
        if t[i] == s[curr_sp_phrase]:
            sp_meter += 1
            curr_sp_phrase += 1
        
        # If the current note is the last note of the current SP phrase, update the SP meter and the current SP phrase
        if t[i] == e[curr_sp_phrase]:
            sp_meter -= 1
            curr_sp_phrase += 1
        
        # If the SP meter is positive, update the current score
        if sp_meter > 0:
            curr_score += 2
        
        # If the current score is higher than the maximum score, update the maximum score
        if curr_score > max_score:
            max_score = curr_score
    
    return max_score

def main():
    n, p, t, s, e = read_input()
    print(find_max_score(n, p, t, s, e))

if __name__ == '__main__':
    main()

