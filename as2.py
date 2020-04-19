import sys

class Fairway:
    def __init__(self, shot, endpoint, probability):
        self.shot = shot
        self.endpoint = endpoint 
        self.probability = probability
    

class Ravine:
    def __init__(self, shot, endpoint, probability):
        self.shot = shot
        self.endpoint = endpoint 
        self.probability = probability

class Over:
    def __init__(self, shot, endpoint, probability):
        self.shot = shot
        self.endpoint = endpoint 
        self.probability = probability

class Same:
    def __init__(self, shot, endpoint, probability):
        self.shot = shot
        self.endpoint = endpoint 
        self.probability = probability

class Left:
    def __init__(self, shot, endpoint, probability):
        self.shot = shot
        self.endpoint = endpoint 
        self.probability = probability

class Close:
    def __init__(self, shot, endpoint, probability):
        self.shot = shot
        self.endpoint = endpoint 
        self.probability = probability

class inputReader():
    def __init__(self):
        pass

    def parseMapFromStdIn(self):
        file = sys.stdin.readlines()
        states = []
        shots = []
        ends = []
        probabilities = []

        i = 0
        for line in file:
            line = line.strip()
            x = line.split("/")
            states.append(x[i])
            shots.append(x[i+1])
            ends.append(x[i+2])
            probabilities.append(x[i+3])
        return (states, shots, ends, probabilities)
            

def main():
    ir = inputReader()
    (states, shots, ends, probabilities) = ir.parseMapFromStdIn()
    print(states)
    print(shots)
    print(ends)
    print(probabilities)

if __name__ == "__main__":
    main()