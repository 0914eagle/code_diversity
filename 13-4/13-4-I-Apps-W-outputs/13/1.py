
import sys
import bisect

class Patient:
    def __init__(self, name, arrival_time, severity):
        self.name = name
        self.arrival_time = arrival_time
        self.severity = severity
        self.priority = severity

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.name < other.name
        return self.priority > other.priority

class Clinic:
    def __init__(self, k):
        self.k = k
        self.patients = []
        self.arrivals = []
        self.departures = []

    def process_arrival(self, patient):
        bisect.insort(self.arrivals, patient.arrival_time)
        self.patients.append(patient)

    def process_departure(self, name):
        try:
            index = next(i for i, p in enumerate(self.patients) if p.name == name)
            patient = self.patients.pop(index)
            self.departures.append(patient.arrival_time)
        except StopIteration:
            pass

    def get_next_patient(self):
        if not self.patients:
            return None
        patient = self.patients[0]
        patient.priority = patient.severity + self.k * (patient.arrival_time - self.departures[-1])
        return patient

def f1(N, K, queries):
    clinic = Clinic(K)
    for query in queries:
        if query[0] == 1:
            clinic.process_arrival(Patient(query[2], query[1], query[3]))
        elif query[0] == 2:
            clinic.process_departure(query[2])
        elif query[0] == 3:
            clinic.process_departure(query[2])
    return clinic.get_next_patient().name if clinic.get_next_patient() else "doctor takes a break"

def f2(N, K, queries):
    clinic = Clinic(K)
    for query in queries:
        if query[0] == 1:
            clinic.process_arrival(Patient(query[2], query[1], query[3]))
        elif query[0] == 2:
            clinic.process_departure(query[2])
        elif query[0] == 3:
            clinic.process_departure(query[2])
    return [patient.name for patient in clinic.patients]

if __name__ == '__main__':
    N, K = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(N)]
    print(f1(N, K, queries))
    print(*f2(N, K, queries), sep='\n')

