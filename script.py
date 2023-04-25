import os
import subprocess
import time

from dotenv import load_dotenv
from tapo_plug import tapoPlugApi

PLUG_DEVICE = "Router smart plug"
TIME_OFF = 2


load_dotenv()

DEVICE = {
    "tapoIp": os.environ["tapoIp"],
    "tapoEmail": os.environ["tapoEmail"],
    "tapoPassword": os.environ["tapoPassword"],
    "nickname": PLUG_DEVICE
}


def main():
    toggle_plug(DEVICE)

    response = tapoPlugApi.getDeviceInfo(DEVICE)
    print(response)


def is_connected():
    try:
        # Ping Google's DNS server
        subprocess.check_output(['ping', '-c', '1', '8.8.8.8'])
        return True
    except subprocess.CalledProcessError:
        return False


def toggle_plug(device):
    print("* %s turned off" % PLUG_DEVICE)
    tapoPlugApi.plugOff(device)

    time.sleep(TIME_OFF)

    print("* %s turned back on after %s seconds" % (PLUG_DEVICE, TIME_OFF))
    tapoPlugApi.plugOn(device)


if __name__ == '__main__':
    main()
