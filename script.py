import os
import time

from dotenv import load_dotenv
from tapo_plug import tapoPlugApi

PLUG_DEVICE = "Router smart plug"
TIME_OFF = 2


def main():
    load_dotenv()

    device = {
        "tapoIp": os.environ["tapoIp"],
        "tapoEmail": os.environ["tapoEmail"],
        "tapoPassword": os.environ["tapoPassword"],
        "nickname": PLUG_DEVICE
    }

    toggle_plug(device)

    response = tapoPlugApi.getDeviceInfo(device)
    print(response)


def toggle_plug(device):
    print("* %s turned off" % PLUG_DEVICE)
    tapoPlugApi.plugOff(device)

    time.sleep(TIME_OFF)

    print("* %s turned back on after %s seconds" % (PLUG_DEVICE, TIME_OFF))
    tapoPlugApi.plugOn(device)


if __name__ == '__main__':
    main()
