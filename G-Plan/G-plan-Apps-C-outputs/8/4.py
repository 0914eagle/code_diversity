ess_events(events, dreams, scenario):
    happened_events = set()
    dream_count = 0
    for event in events:
        if event.startswith('E'):
            happened_events.add(event[2:])
        elif event.startswith('D'):
            dream_count += int(event[2:])
        else:
            scenario_events = set(event.split()[2:])
            for e in scenario_events:
                if e.startswith('!'):
                    e = e[1:]
                    if e in happened_events or dream_count > 0:
                        return "Plot Error"
                else:
                    if e not in happened_events:
                        return "Plot Error"
    return "Yes" if dream_count == 0 else f"{dream_count} Just A Dream"


if __name__ == '__main__':
    n = int(input())
    events = []
    dreams = []
    scenarios = []
    for _ in range(n):
        line = input().strip()
        if line.startswith('E') or line.startswith('D'):
            events.append(line)
        else:
            scenarios.append(line)

    for scenario in scenarios:
        result = process_events(events, dreams, scenario)
        print(result)
