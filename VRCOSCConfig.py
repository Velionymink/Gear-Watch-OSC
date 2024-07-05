from pythonosc import udp_client


class VRCOSCConfig:
    def __init__(self):
        self.osc_ip = "127.0.0.1"
        self.osc_port = 9000
        self.osc_client = udp_client.SimpleUDPClient(self.osc_ip, self.osc_port)

    def send_osc_message(self, address, value):
        self.osc_client.send_message(address, value)
