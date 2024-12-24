from toy_factory import ToyFactory

def main():
    toy_types = ["car", "doll", "puzzle", "unknown"]

    for toy_type in toy_types:
        try:
            toy = ToyFactory.create_toy(toy_type)
            print(f"Created a {toy_type.capitalize()} Toy. Playing: {toy.play()}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()