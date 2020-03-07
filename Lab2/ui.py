class UI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        n = int(input("size: "))
        self.controller.problem.setN(n)
        print("1. DFS")
        print("2. GREEDY")
        number = int(input("Choose technique:"))
        print("Computing...")
        if number == 1:
            result = self.controller.dfs()
            if result is None:
                print("No result found!")
                return
            print(result)
        elif number == 2:
            result = self.controller.greedy()
            if result is None:
                print("No result found!")
                return
            print(result)
        else:
            print("Invalid number!")
