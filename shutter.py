import evdev
from time import sleep

from unicornhat import UnicornHatHD


emoji = "microphone"

def get_device():
    print("Waiting for BT Shutter to be ready...")

    while(True):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if("BT Shutter Consumer Control" in device.name):
                dev = evdev.InputDevice(device.path)

                print(f"Ready: {dev}\n")
                return dev
        sleep(0.1)


def run():
    hat = UnicornHatHD()
    while True:
        dev = get_device()
        try:
            timestamp = 0
            for event in dev.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                    if event.value == 1:
                        hat.draw_emoji(emoji)
                    elif event.value == 0 and event.timestamp()-timestamp < 2.0:
                        hat.clear()

                    print(evdev.categorize(event))
                    timestamp= event.timestamp()

        except Exception as e:
            print(f"Disconnected from BT Shutter: {e}\n")


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
