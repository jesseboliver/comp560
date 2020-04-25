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

def Shoot(states, shots, ends, probabilities, currState, all):
    probabilitylist = []
    shotlist = []
    endlist = []
    state = ''
    shot = ''
    visited = {}
    '''
    if all == True:
        for i in range(len(states)):
            shot = shots[i]
            state = states[i]
            if state in visited and shot == visited[state]:
                i+=1
                continue
            visited.update({state:shot})
            for i in range(len(states)):
                if states[i] == state:
                    if shots[i] == shot:
                        shotlist.append(shots[i])
                        probabilitylist.append((probabilities[i]))
                        endlist.append(ends[i])
            probabilitylist = [float(i) for i in probabilitylist]
            x = np.random.choice(endlist, 50, p=probabilitylist)
            print('State: ', state,',', 'Shot : ', shot,',', 'Visited: ', x)

            endlist.clear()
            probabilitylist.clear()
        return 
    else:
        '''
    state = currState
    for i in range(len(states)):
        if states[i] == state:
            if shots[i] not in shotlist:
                shotlist.append(shots[i])
    shotchoice = np.random.choice(shotlist)
    for i in range(len(states)):
        if states[i] == state:
            if shots[i] == shotchoice:
                probabilitylist.append(probabilities[i])
                endlist.append(ends[i])
    print(shotchoice) 
    print(probabilitylist)
    print(endlist)
    nextState = np.random.choice(endlist, 1, p=probabilitylist)
    print('State: ', state,',', 'Shot : ', shotchoice,',', 'NextState: ', nextState)
    return nextState, shotchoice


def ModelFreeLearning(states, shots, ends, probabilities):
    # 4 values for utility function aligned in several arrays:
    StateUtil = {}
    for i in range(len(states)):
        StateUtil.update({states[i] : 1})
    print(StateUtil)
    ActionUtil = {}
    for i in range(len(shots)):
        ActionUtil.update({shots[i] : 1})
    SprimeUtil = []
    print(ActionUtil)
    rewardUtil = []
    currState = 'Fairway'
    #StateUtil.append(currState)
    newState, action = Shoot(states, shots, ends, probabilities, currState, False)
    #ActionUtil.append(action)
    SprimeUtil.append(newState)
    # reward is always 1 for reaching new state. 0 for reaching same state
    finished = False
    while not finished:
        for i in range(len(states)):
            q_value = []
            looping = True
            while looping:
                next_state_reward = []
                for action in shots[i]:
                    

def main():
    print(random())
    ir = inputReader()
    (states, shots, ends, probabilities) = ir.parseMapFromStdIn()
    '''
    print(states)
    print(shots)
    print(ends)
    print(probabilities)
    '''
    ModelFreeLearning(states, shots, ends, probabilities)

if __name__ == "__main__":
    main()