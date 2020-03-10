from Lab2.problem import Problem
from Lab2.state import State


class Controller:
    def __init__(self, problem: Problem):
        self.problem = problem

    def orderStates(self, states):
        aux = [(x, self.problem.heuristic(x)) for x in states]
        aux.sort(key=lambda t: t[1])
        return [x[0] for x in aux]

    def dfs(self):
        stack = [self.problem.initialState()]

        while len(stack) > 0:
            currentState = stack.pop()
            if self.problem.checkFinalState(currentState):
                return currentState
            stack = stack + self.problem.expandState(currentState)
        return None

    def greedy(self):
        toCheck = [self.problem.initialState()]
        while len(toCheck) > 0:
            state = toCheck.pop(0)
            if self.problem.checkFinalState(state):
                return state
            toCheck = self.orderStates(self.problem.expandState(state))
        return None
