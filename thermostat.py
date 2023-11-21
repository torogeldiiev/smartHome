from devices import Devices

class Thermostat(Devices):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 0
        self.__device_type = "Thermostat"

    def set_temperature(self, temp):
        if temp > 0:
            self.turn_on()
            self.temperature = temp
        else:
            self.turn_off()
            self.temperature = temp

    @property
    def device_type(self):
        return self.__device_type