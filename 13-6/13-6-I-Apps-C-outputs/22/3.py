
def get_implications(n, m):
    implications = []
    for i in range(m):
        a, b = map(int, input().split())
        implications.append((a, b))
    return implications

def get_known_events(n, m):
    known_events = set()
    for i in range(m):
        event = int(input())
        known_events.add(event)
    return known_events

def get_causal_events(implications, known_events):
    causal_events = set()
    for a, b in implications:
        if b in known_events:
            causal_events.add(a)
    return causal_events

def get_certain_events(causal_events, known_events):
    certain_events = causal_events.intersection(known_events)
    return certain_events

def main():
    n, m, k = map(int, input().split())
    implications = get_implications(n, m)
    known_events = get_known_events(n, k)
    causal_events = get_causal_events(implications, known_events)
    certain_events = get_certain_events(causal_events, known_events)
    print(*sorted(certain_events), sep=' ')

if __name__ == '__main__':
    main()

