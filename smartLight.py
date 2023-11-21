from devices import Devices

class SmartLight(Devices):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.__brightness = 0
        self.__device_type = "SmartLight"

    @property
    def brightness(self):
        return self.__brightness

    @property
    def device_type(self):
        return self.__device_type

    def adjust_brightness(self, brightness: float):
        if brightness > 0:
            self.turn_on()
        self.__brightness = brightness
        if brightness == 0:
            self.turn_off()

    def gradual_dimming(self, target_brightness: int, duration: float):
        steps = (self.brightness - target_brightness) / duration
        while self.brightness > target_brightness:
            self.adjust_brightness(self.brightness - steps)
            time.sleep(1)