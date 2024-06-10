ess_event(event, events, dreams):
    if event[0] == 'E':
        events.add(event[1])
    elif event[0] == 'D':
        for _ in range(event[1]):
            last_event = events.pop()
            dreams.add(last_event)

def is_scenario_consistent(scenario, events, dreams):
    for event in scenario[2:]:
        if event[0] == '!':
            if event[1:] in events or event[1:] not in dreams:
                return False
        else:
            if event not in events or event in dreams:
                return False
    return True

def process_scenarios(n, lines):
    events = set()
    dreams = set()
    for i in range(n):
        line = lines[i]
        if line[0] == 'E' or line[0] == 'D':
            process_event(line, events, dreams)
        elif line[0] == 'S':
            if is_scenario_consistent(line, events, dreams):
                print("Yes")
            else:
                for r in range(1, len(events) + 1):
                    events_copy = events.copy()
                    dreams_copy = dreams.copy()
                    if process_event(('D', r), events_copy, dreams_copy):
                        if is_scenario_consistent(line, events_copy, dreams_copy):
                            print(f"{r} Just A Dream")
                            break
                else:
                    print("Plot Error")

if __name__ == "__main__":
    n = int(input())
    lines = [input().split() for _ in range(n)]
    process_scenarios(n, lines)
