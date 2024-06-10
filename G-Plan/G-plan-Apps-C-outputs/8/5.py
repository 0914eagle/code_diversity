ess_event(event, events, dreams):
    if event[0] == 'E':
        events.append(event[2:])
    elif event[0] == 'D':
        for _ in range(int(event[2:])):
            if events:
                dreams.append(events.pop())
    return events, dreams

def is_scenario_possible(scenario, events, dreams):
    current_events = events.copy()
    current_dreams = dreams.copy()
    
    for event in scenario[2:]:
        if event[0] == '!':
            if event[1:] in current_events or event[1:] in current_dreams:
                return False
        else:
            if event not in current_events:
                return False
    return True

def process_scenario(scenario, events, dreams):
    if is_scenario_possible(scenario, events, dreams):
        return "Yes"
    
    for i in range(1, len(events) + 1):
        temp_events = events[:len(events) - i]
        temp_dreams = events[len(events) - i:] + dreams
        if is_scenario_possible(scenario, temp_events, temp_dreams):
            return f"{i} Just A Dream"
    
    return "Plot Error"

if __name__ == "__main__":
    n = int(input())
    events = []
    dreams = []
    
    for _ in range(n):
        line = input().split()
        if line[0] == 'S':
            scenario = line
            result = process_scenario(scenario, events, dreams)
            print(result)
        else:
            events, dreams = process_event(line, events, dreams)
