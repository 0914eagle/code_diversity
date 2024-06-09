
import sys

class Patient:
    def __init__(self, name, severity, arrival_time):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time
        self.wait_time = 0

    def __lt__(self, other):
        return (self.severity + K * self.wait_time, self.name) < (other.severity + K * other.wait_time, other.name)

class Clinic:
    def __init__(self, k):
        self.k = k
        self.patients = []

    def process_arrival(self, patient):
        self.patients.append(patient)

    def process_notification(self, name):
        for i in range(len(self.patients)):
            if self.patients[i].name == name:
                self.patients.pop(i)
                break

    def process_query(self, time):
        while self.patients and self.patients[0].arrival_time <= time:
            patient = self.patients.pop(0)
            patient.wait_time += 1
            self.patients.append(patient)
        if self.patients:
            return self.patients[0].name
        else:
            return "doctor takes a break"

K = None
patients = []

def f1(time, name, severity):
    global K
    K = severity
    patient = Patient(name, severity, time)
    patients.append(patient)

def f2(time):
    global patients
    return patients[0].name if patients else "doctor takes a break"

def f3(time, name):
    global patients
    for i in range(len(patients)):
        if patients[i].name == name:
            patients.pop(i)
            break

if __name__ == '__main__':
    n, k = map(int, input().split())
    for _ in range(n):
        q, *args = input().split()
        if q == "1":
            f1(*map(int, args))
        elif q == "2":
            print(f2(int(args[0])))
        elif q == "3":
            f3(*map(int, args))

