from script import is_connected, toggle_plug, DEVICE

PLUG_DEVICE = "Router smart plug"
TIME_OFF = 2


def main():
    if is_connected():
        print("We're still connected, yay!")
    else:
        print("Whoops, it seems we lost the connection...")
        toggle_plug(DEVICE)


if __name__ == '__main__':
    main()
