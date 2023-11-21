from devices import Devices

class SecurityCamera(Devices):
    def __init__(self, device_id: str):
        super().__init__(device_id)
        self.__securityStatus = "NO"
        self.__device_type = "SecurityCamera"

    @property
    def device_type(self):
        return self.__device_type

    def get_security_status(self):
        return self.__securityStatus

    def set_security_status(self, status):
        self.__securityStatus = status
