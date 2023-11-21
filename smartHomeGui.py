from smartLight import SmartLight
from thermostat import Thermostat
from securityCamera import SecurityCamera

import random
import time
import threading
import tkinter as tk


class SmartHomeGUI(tk.Tk):
    def __init__(self, automation_system):
        super().__init__()

        self.brightness_level_label = tk.Label(
            self,
            text="Living room Light - 0"
        )
        self.title("Smart Home IoT Simulator")
        self.geometry("700x700")

        self.automation_system = automation_system

        self.create_title_label()
        self.create_devices_status_text()
        self.create_devices()

        self.create_brightness_widgets()
        self.create_thermostat_widgets()
        self.create_security_camera_widgets()

    def create_title_label(self):
        title_label = tk.Label(
            self,
            text="Smart Home",
            font=("Times new Roman", 14, "bold")
        )
        title_label.pack(pady=20)

    def create_devices_status_text(self):
        self.devices_status_text = tk.Text(self, height=10, width=50)
        self.devices_status_text.pack(side="top")

    def create_devices(self):
        self.smart_light = SmartLight("Living room light")
        self.thermostat = Thermostat("Living room thermostat")
        self.security_camera = SecurityCamera("Main entrance camera")

        self.smart_light_status_var = tk.StringVar()
        self.smart_light_status_var.set(f"SmartLight Status:{self.smart_light.status}")

        self.thermostat_status_var = tk.StringVar()
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")

        self.security_camera_status_var = tk.StringVar()
        self.security_camera_status_var.set(f"Camera Status: {self.security_camera.status}")
        self.display_current_devices()

    def create_brightness_widgets(self):
        living_room_brightness_label = tk.Label(
            self,
            text="Living Room Brightness",
            font=("Helvetica", 10),
        )
        living_room_brightness_label.pack(pady=1, side="top")

        self.brightness_scale = tk.Scale(
            self,
            from_=0,
            to=90,
            orient=tk.HORIZONTAL,
            length=100,
            sliderlength=30,
            command=self.update_brightness,
        )
        self.brightness_scale.pack(pady=1)

        toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            command=self.toggle_smart_light,
        )
        toggle_button.pack(pady=1)

        self.brightness_level_label.pack(pady=1, side="top")

    def create_thermostat_widgets(self):
        thermostat_temperature_label = tk.Label(
            self,
            text="Living Room Thermostat Temperature",
            font=("Helvetica", 10),
        )
        thermostat_temperature_label.pack(pady=1, side="top")

        self.temperature_scale = tk.Scale(
            self,
            from_=0,
            to=90,
            orient=tk.HORIZONTAL,
            length=100,
            sliderlength=30,
            command=self.update_temperature,
        )
        self.temperature_scale.pack(pady=1)

        thermostat_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            command=self.toggle_thermostat,
        )
        thermostat_toggle_button.pack(pady=1)

        self.temperature_level_label = tk.Label(
            self,
            text="Living room thermostat: 0",
        )
        self.temperature_level_label.pack(pady=5, side="top")

    def create_security_camera_widgets(self):
        security_camera_status_label = tk.Label(
            self,
            text="Front Door Camera Motion Detection",
            font=("Helvetica", 10),
        )
        security_camera_status_label.pack(pady=1, side="top")

        motion_button = tk.Button(
            self,
            text="Random Detect Motion",
            command=self.toggle_motion
        )
        motion_button.pack(pady=10)

        security_camera_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            command=self.toggle_security_camera,
        )
        security_camera_toggle_button.pack(pady=1)

        self.motion_status_label = tk.Label(
            self,
            text="Front Door Camera - Motion: NO",
        )
        self.motion_status_label.pack(pady=1, side="top")

    def update_brightness(self, value):
        self.smart_light.adjust_brightness(float(value))
        self.brightness_level_label["text"] = f"Brightness Level: {value}"
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")
        self.update_device_status_text()

    def update_temperature(self, value):
        self.thermostat.set_temperature(float(value))
        self.temperature_level_label["text"] = f"Temperature Level: {value}"
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")
        self.update_device_status_text()

    def update_device_status_text(self):
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat, self.security_camera]
        for device in devices:
            status_info = f"{device.id}: {device.device_type} Status: {device.status}"
            self.devices_status_text.insert(tk.END, status_info + "\n")

    def toggle_smart_light(self):
        if self.smart_light.status == "On":
            self.smart_light.turn_off()
            self.smart_light.adjust_brightness(0)
        else:
            self.smart_light.turn_on()

        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")
        self.brightness_scale.set(self.smart_light.brightness)
        self.update_device_status_text()

    def toggle_thermostat(self):
        if self.thermostat.status == "On":
            self.thermostat.turn_off()
            self.thermostat.set_temperature(0)
        else:
            self.thermostat.turn_on()

        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")
        self.temperature_scale.set(self.thermostat.temperature)
        self.update_device_status_text()

    def toggle_security_camera(self):
        if self.security_camera.status == "On":
            self.security_camera.turn_off()
            self.security_camera.set_security_status("Off")
        else:
            self.security_camera.turn_on()

        self.security_camera_status_var.set(
            "On" if self.security_camera.status == "YES" else "NO"
        )
        self.update_device_status_text()

    def toggle_motion(self):
        if self.security_camera.status == "On":
            status = random.choice(["YES", "NO"])
            self.security_camera.set_security_status(status)
            self.motion_status_label["text"] = f"Motion Status: {status}"
        else:
            self.motion_status_label["text"] = "Motion Status: OFF"

        self.update_device_status_text()

    def display_current_devices(self):
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat, self.security_camera]
        for device in devices:
            self.devices_status_text.insert(tk.END, f"{device.id}: {device.device_type} Status: {device.status}\n")

    def simulation_loop(self):
        try:
            while True:
                self.automation_system.execute_automation_tasks()
                self.update_device_status_text()
                time.sleep(5)
        except KeyboardInterrupt:
            print("Simulation stopped by the user.")

    def run_simulation_loop(self):
        try:
            self.simulate_random_events()

            self.automation_system.execute_automation_tasks()

            self.update_device_status_text()

            self.after(5000, self.run_simulation_loop)
        except KeyboardInterrupt:
            print("Simulation stopped by the user.")

    def simulate_random_events(self):
        if self.smart_light.status == "On" and random.random() < 0.99:
            brightness_value = random.randint(0, 100)
            self.smart_light.adjust_brightness(brightness_value)
            self.brightness_level_label["text"] = f"Brightness Level: {brightness_value}"
            self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")

        if self.thermostat.status == "On" and random.random() < 0.99:
            temperature_value = random.randint(0, 40)
            self.thermostat.set_temperature(temperature_value)
            self.temperature_level_label["text"] = f"Temperature Level: {temperature_value}"
            self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")

    def start_simulation(self):
        simulation_thread = threading.Thread(target=self.run_simulation_loop)
        simulation_thread.start()

    def run(self):
        self.after(100, self.run_simulation_loop)
        super().run()
