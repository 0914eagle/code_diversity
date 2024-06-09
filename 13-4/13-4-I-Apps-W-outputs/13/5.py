
import sys

class Patient:
    def __init__(self, name, arrival_time, severity):
        self.name = name
        self.arrival_time = arrival_time
        self.severity = severity
        self.wait_time = 0

    def __lt__(self, other):
        if self.severity == other.severity:
            return self.name < other.name
        return self.severity > other.severity

class Clinic:
    def __init__(self, k):
        self.k = k
        self.patients = []

    def process_arrival(self, patient):
        self.patients.append(patient)

    def process_ready(self, current_time):
        if not self.patients:
            return "doctor takes a break"
        patient = self.patients[0]
        patient.wait_time += current_time - patient.arrival_time
        return patient.name

    def process_leave(self, name):
        for i, patient in enumerate(self.patients):
            if patient.name == name:
                self.patients.pop(i)
                break

def f1(k, queries):
    clinic = Clinic(k)
    for query in queries:
        if query[0] == 1:
            clinic.process_arrival(Patient(query[2], query[1], query[3]))
        elif query[0] == 2:
            print(clinic.process_ready(query[1]))
        else:
            clinic.process_leave(query[2])

def f2(k, queries):
    clinic = Clinic(k)
    for query in queries:
        if query[0] == 1:
            clinic.process_arrival(Patient(query[2], query[1], query[3]))
        elif query[0] == 2:
            print(clinic.process_ready(query[1]))
        else:
            clinic.process_leave(query[2])

if __name__ == '__main__':
    k = int(input())
    queries = []
    for _ in range(int(input())):
        queries.append(list(map(int, input().split())))
    f1(k, queries)
    f2(k, queries)

