from subject import Subject

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temparature = None
    
    def set_temperature(self, temparature):
        self._temparature = temparature
        print(f"WeatherStation: Temperature set to {self._temparature}°C.")
        self.notify(self._temparature)
    
    def get_temparature(self):
        return self._temparature