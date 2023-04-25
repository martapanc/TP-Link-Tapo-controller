import os

from dotenv import load_dotenv
from tapo_plug import tapoPlugApi


def main():
    load_dotenv()

    device = {
        "tapoIp": os.environ["tapoIp"],
        "tapoEmail": os.environ["tapoEmail"],
        "tapoPassword": os.environ["tapoPassword"]
    }

    response = tapoPlugApi.getDeviceInfo(device)
    print(response)


if __name__ == '__main__':
    main()
