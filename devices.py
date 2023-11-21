

class Devices:
    def __init__(self, device_id: str):
        self.__device_id = device_id
        self.__status = "Off"

    @property
    def status(self):
        return self.__status

    @property
    def id(self):
        return self.__device_id

    def turn_on(self):
        if self.__status == "Off":
            self.__status = "On"

    def turn_off(self):
        if self.__status == "On":
            self.__status = "Off"