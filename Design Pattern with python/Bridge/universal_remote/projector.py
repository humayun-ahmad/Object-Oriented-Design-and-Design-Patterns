from device import Device

class Projector(Device):
    def __init__(self):
        self.brightness = 50

    def turn_on(self):
        print("Projector is now ON.")

    def turn_off(self):
        print("Projector is now OFF.")

    def increase_volume(self):
        print("Projectors don't have volume, but brightness is increased instead.")
        self.brightness += 10
        print(f"Projector brightness increased to {self.brightness}.")

    def decrease_volume(self):
        print("Projectors don't have volume, but brightness is decreased instead.")
        self.brightness -= 10
        print(f"Projector brightness decreased to {self.brightness}.")