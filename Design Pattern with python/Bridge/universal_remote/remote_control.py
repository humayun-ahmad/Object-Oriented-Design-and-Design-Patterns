class RemoteControl:
    def __init__(self, device):
        self.device = device
    
    def power_on(self):
        self.device.turn_on()
    
    def power_off(self):
        self.device.turn_off()
    
    def volume_up(self):
        self.device.increase_volume()
    
    def volume_down(self):
        self.device.decrease_volume()