import time
from datetime import datetime
import VRCOSCConfig


def main():
    config = VRCOSCConfig.VRCOSCConfig()

    update_watch(config)


def update_watch(config):
    ticking = False

    while True:
        now = datetime.now()

        seconds = now.second / 60.0
        minutes = (now.minute + seconds) / 60.0
        hours = (now.hour % 24 + minutes) / 24.0

        # Send OSC messages to update the watch
        config.send_osc_message("/avatar/parameters/SecondHand_OSC", seconds)
        config.send_osc_message("/avatar/parameters/MinuteHand_OSC", minutes)
        config.send_osc_message("/avatar/parameters/HourHand_OSC", hours)
        config.send_osc_message("/avatar/parameters/TickingSound_OSC", ticking)

        # Wait until the next second
        time.sleep(1 - now.microsecond / 1000000.0)
        ticking = not ticking


if __name__ == "__main__":
    main()
