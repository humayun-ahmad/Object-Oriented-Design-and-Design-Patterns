class Toy:
    def play(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class CarToy(Toy):
    def play(self):
        return "Vroom! The car is driving."

class DollToy(Toy):
    def play(self):
        return "Rolling on the floor, the doll is happy."

class PuzzleToy(Toy):
    def play(self):
        return "Solving puzzles, the puzzle is fun."
