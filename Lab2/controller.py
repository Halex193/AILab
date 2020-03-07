from Lab2.problem import Problem


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
        visited = []
        toVisit = [self.problem.initialState()]
        while len(toVisit) > 0:
            state = toVisit.pop(0)
            visited.append(state.lastBoard())
            if self.problem.checkFinalState(state):
                return state
            aux = []
            for x in self.problem.expandState(state):
                if x.lastBoard() not in visited:
                    aux.append(x)
            toVisit = self.orderStates(aux) + toVisit
        return None
