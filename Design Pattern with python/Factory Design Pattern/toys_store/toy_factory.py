from toys import CarToy, DollToy, PuzzleToy

class ToyFactory:
    
    @staticmethod
    def create_toy(toy_type):
        if toy_type == "car":
            return CarToy()
        elif toy_type == "doll":
            return DollToy()
        elif toy_type == "puzzle":
            return PuzzleToy()
        else:
            raise ValueError(f"Toy type: {toy_type}")
        

