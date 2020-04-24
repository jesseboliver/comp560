import sys
from random import random
from collections import defaultdict
import numpy as np
#kgnu33

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

def Putt(states, shots, ends, probabilities, shotlist, probabilitylist, endlist, state, shot):
    for i in range(len(states)):
        if states[i] == state:
            if shots[i] == shot:
                shotlist.append(shots[i])
                probabilitylist.append((probabilities[i]))
                endlist.append(ends[i])
    probabilitylist = [float(i) for i in probabilitylist]
    return endlist, probabilitylist
            

def main():
    print(random())
    ir = inputReader()
    (states, shots, ends, probabilities) = ir.parseMapFromStdIn()
    print(states)
    print(shots)
    print(ends)
    print(probabilities)
    probabilitylist = []
    shotlist = []
    endlist = []
    state = ''
    shot = ''
    visited = {}
    for i in range(len(states)):
        shot = shots[i]
        state = states[i]
        if state in visited and shot == visited[state]:
            i+=1
            continue
        visited.update({state:shot})
        endlist, probabilitylist = Putt(states, shots, ends, probabilities, shotlist, probabilitylist, endlist, state, shot)
        #print('State: ', state,',', 'Shot : ', shot,', ', 'endlist: ', endlist, ' ProbabilityList: ', p=probabilitylist)
        x = np.random.choice(endlist, 50, p=probabilitylist)
        print('State: ', state,',', 'Shot : ', shot,',', 'Visited: ', x)

        endlist.clear()
        probabilitylist.clear()


if __name__ == "__main__":
    main()