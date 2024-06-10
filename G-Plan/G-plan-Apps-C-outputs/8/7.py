ess_input():
    n = int(input())
    events = []
    dreams = []
    scenarios = []
    
    for _ in range(n):
        line = input().split()
        if line[0] == 'E':
            events.append(line[1])
        elif line[0] == 'D':
            dreams.append(int(line[1]))
        elif line[0] == 'S':
            scenarios.append((int(line[1]), line[2:]))
    
    return events, dreams, scenarios

def check_scenario(events, dreams, scenario):
    current_events = events.copy()
    for dream in dreams:
        current_events = current_events[:-dream]
    
    for event in scenario[1]:
        if event[0] == '!':
            if event[1:] in current_events:
                return False
        else:
            if event not in current_events:
                return False
    
    return True

if __name__ == "__main__":
    events, dreams, scenarios = process_input()
    
    for scenario in scenarios:
        if check_scenario(events, dreams, scenario):
            print("Yes")
        else:
            consistent_with_dream = False
            for r in range(1, len(events) + 1):
                if check_scenario(events, dreams + [r], scenario):
                    consistent_with_dream = True
                    print(f"{r} Just A Dream")
                    break
            if not consistent_with_dream:
                print("Plot Error")
