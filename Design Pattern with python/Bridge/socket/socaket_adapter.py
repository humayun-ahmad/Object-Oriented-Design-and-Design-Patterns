class EuropeanToAmericanAdapter:

    def __init__(self, european_socket):
        self._european_socket = european_socket

    def voltage(self):
        return 120  # converts to 120V, compatible with AmericanSocket

    def live(self):
        return self._european_socket.live()

    def neutral(self):
        return self._european_socket.neutral()

