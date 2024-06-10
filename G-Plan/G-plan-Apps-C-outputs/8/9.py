ess_event(event, events, dreams):
    if event[0] == 'E':
        events.add(event[1])
    elif event[0] == 'D':
        for _ in range(event[1]):
            last_event = events.pop()
            dreams.add(last_event)

def check_scenario(scenario, events, dreams):
    scenario_events = set(scenario[2:])
    for event in scenario[2:]:
        if event.startswith('!'):
            if event[1:] in events or event[1:] in dreams:
                return "Plot Error"
        else:
            if event not in events and event not in dreams:
                return "Plot Error"
    return "Yes"

def process_input(n, lines):
    events = set()
    dreams = set()
    for i in range(1, n+1):
        line = lines[i].split()
        if line[0] == 'E':
            process_event(('E', line[1]), events, dreams)
        elif line[0] == 'D':
            process_event(('D', int(line[1])), events, dreams)
        elif line[0] == 'S':
            result = check_scenario(line, events, dreams)
            if result == "Plot Error":
                print("Plot Error")
            else:
                print(result)

if __name__ == "__main__":
    n = int(input())
    lines = [input() for _ in range(n)]
    process_input(n, lines)
