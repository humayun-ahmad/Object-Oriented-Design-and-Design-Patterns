from device import Device

class TV(Device):
    def __init__(self):
        self.volume = 10

    def turn_on(self):
        print("TV is now ON.")

    def turn_off(self):
        print("TV is now OFF.")

    def increase_volume(self):
        self.volume += 1
        print(f"TV volume increased to {self.volume}.")

    def decrease_volume(self):
        self.volume -= 1
        print(f"TV volume decreased to {self.volume}.")