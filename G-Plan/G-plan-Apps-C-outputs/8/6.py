ess_scenario(events, scenario):
    current_events = set()
    for event in events:
        if event.startswith('!'):
            current_events.discard(event[1:])
        else:
            current_events.add(event)
    
    for event in scenario[2:]:
        if event.startswith('!') and event[1:] in current_events:
            return "Plot Error"
        elif not event.startswith('!') and event[1:] not in current_events:
            return "Plot Error"
    
    return "Yes"

def handle_dream(events, dream_count):
    return events[:-dream_count]

if __name__ == "__main__":
    n = int(input())
    events = []
    
    for _ in range(n):
        line = input().split()
        if line[0] == 'E':
            events.append(line[1])
        elif line[0] == 'D':
            events = handle_dream(events, int(line[1]))
        elif line[0] == 'S':
            result = process_scenario(events, line)
            print(result)
