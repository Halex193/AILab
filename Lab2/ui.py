class UI:
    def __init__(self, controller):
        self.controller = controller

    def mainMenu(self):
        print("1. DFS")
        print("2. GREEDY")
        number = int(input("Choose technique:"))
        if number == 1:
            self.controller.dfs()
        elif number == 1:
            self.controller.greedy()
        else:
            print("Invalid number!")
