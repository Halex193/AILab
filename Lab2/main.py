from Lab2.controller import Controller
from Lab2.problem import Problem
from Lab2.ui import UI

if __name__ == '__main__':
    problem = Problem()
    controller = Controller(problem)
    ui = UI(controller)
    ui.run()
