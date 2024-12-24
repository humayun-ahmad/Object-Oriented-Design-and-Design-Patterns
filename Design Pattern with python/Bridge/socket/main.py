from socaket_adapter import EuropeanToAmericanAdapter
from socket import EuropeanSocket, AmericanSocket

# Usage

european_socket = EuropeanSocket()
adapter = EuropeanToAmericanAdapter(european_socket)
american_socket = AmericanSocket()

# Using the adapter to make european socket compatible with American socket interface
print(f"Adapted voltage: {adapter.voltage()}V")  # Output: Adapted voltage: 120V