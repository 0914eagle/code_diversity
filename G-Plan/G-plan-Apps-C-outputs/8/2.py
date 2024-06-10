ess_event(event, events, dreams):
    if event[0] == 'E':
        events.append(event[2:])
    elif event[0] == 'D':
        num_dreams = int(event[2:])
        for _ in range(num_dreams):
            if events:
                dreams.append(events.pop())
    return events, dreams

def check_scenario(scenario, events, dreams):
    scenario_events = scenario[2:]
    for event in scenario_events:
        if event[0] == '!':
            if event[1:] in events or event[1:] in dreams:
                return False
        else:
            if event not in events:
                return False
    return True

def process_scenarios(n, lines):
    events = []
    dreams = []
    for _ in range(n):
        line = lines.pop(0)
        if line[0] == 'E' or line[0] == 'D':
            events, dreams = process_event(line, events, dreams)
        elif line[0] == 'S':
            if check_scenario(line, events, dreams):
                print("Yes")
            else:
                for i in range(1, len(events) + 1):
                    temp_events = events.copy()
                    temp_dreams = dreams.copy()
                    consistent = True
                    for j in range(i):
                        if temp_events:
                            temp_dreams.append(temp_events.pop())
                        else:
                            consistent = False
                            break
                    if consistent and check_scenario(line, temp_events, temp_dreams):
                        print(f"{i} Just A Dream")
                        break
                else:
                    print("Plot Error")

if __name__ == "__main__":
    n = int(input())
    lines = [input().split() for _ in range(n)]
    process_scenarios(n, lines)
