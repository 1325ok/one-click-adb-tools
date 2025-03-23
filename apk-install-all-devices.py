import os
import sys
from adbutils import adb

def get_connected_devices_serials():
    devices = adb.device_list()
    serials = [device.serial for device in devices]
    return serials

def install_apk_on_all_devices(apk_path):
    if not os.path.exists(apk_path):
        print(f"Error: APK file '{apk_path}' not found.")
        return

    serials = get_connected_devices_serials()
    if not serials:
        print("No connected devices found.")
        return

    for serial in serials:
        print(f"Installing APK on device {serial}...")
        device = adb.device(serial)
        device.install(apk_path)
        print(f"APK installed on device {serial}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python apk-install-all-devices.py <apk_file_path>")
        sys.exit(1)

    apk_path = sys.argv[1]
    install_apk_on_all_devices(apk_path)

    