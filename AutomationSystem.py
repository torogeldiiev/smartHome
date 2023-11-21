from thermostat import Thermostat
from smartHomeGui import SmartHomeGUI
class AutomationSystem:
    def __init__(self):
        self.devices = []

    def discover_device(self, device):
        if device not in self.devices:
            self.devices.append(device)

    def execute_automation_tasks(self):
        for device in self.devices:
            if isinstance(device, Thermostat):
                self.automate_thermostat(device)

    def automate_thermostat(self, thermostat):
        pass

automation_system = AutomationSystem()
gui = SmartHomeGUI(automation_system)
gui.start_simulation()
gui.mainloop()