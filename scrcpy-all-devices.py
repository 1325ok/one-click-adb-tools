import subprocess
from adbutils import adb

def list_all_devices_and_run_scrcpy():
    devices = adb.device_list()
    if not devices:
        print("No devices connected.")
    else:
        print("Connected devices:")
        for device in devices:
            print(f"Serial: {device.serial}")
            try:
                # Run scrcpy for each device
                subprocess.Popen(["scrcpy", "-s", device.serial])
            except FileNotFoundError:
                print("scrcpy is not installed or not in PATH.")

if __name__ == "__main__":
    list_all_devices_and_run_scrcpy()