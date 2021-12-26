# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
Client
"""
from typing import List, Tuple

# from enum import IntEnum
import random
import sys
import socket
import time


class MyPacket:
    """
    <-----                            32 bit                              ----->
    |--------------------------------------------------------------------------|
    |       Message ID (Service ID [16 bit] / Method ID [16 bit]) [32 bit]     |
    |--------------------------------------------------------------------------|
    |                        Length [32 bit]                                   |
    |--------------------------------------------------------------------------|
    |       Request ID (Client ID [16 bit] / Session ID [16 bit]) [32 bit]     |
    |--------------------------------------------------------------------------|
    | Protocol Ver.[8 bit] IF. Ver.[8 bit] Msg. Type[8 bit] Return Code [8 bit]|
    |--------------------------------------------------------------------------|
    |                           Payload [variable size]                        |
    |--------------------------------------------------------------------------|

    """

    class Header:
        class MessageID:
            class ServiceID:
                """
                2 bytes
                """

                DEFAULT = 0x1001

            class MethodID:
                """
                2 bytes
                """

                DEFAULT = 0x2001

            def __init__(
                self,
                service_id: int = ServiceID.DEFAULT,
                method_id: int = MethodID.DEFAULT,
            ) -> None:
                self._msg_id: Tuple[int, int] = (service_id, method_id)

            def get_msg_id(self) -> Tuple[int, int]:
                return self._msg_id

        class RequestID:
            class ClientID:
                """
                2 bytes
                """

                DEFAULT = 0x3001

            class SessionID:
                """
                2 bytes
                """

                DEFAULT = 0x4001

            def __init__(
                self,
                client_id: int = ClientID.DEFAULT,
                session_id: int = SessionID.DEFAULT,
            ) -> None:
                self._request_id: Tuple[int, int] = (client_id, session_id)

            def get_request_id(self) -> Tuple[int, int]:
                return self._request_id

        class ProtocolVersion:
            DEFAULT: int = 0x01

        class InterfaceVersion:
            DEFAULT: int = 0x01

        class MessageType:
            REQUEST: int = 0x00
            RESPONSE: int = 0x80

        def set_message_type(self, type: MessageType):
            self._message_type = type

        def get_message_type(self) -> MessageType:
            return self._message_type

        class ReturnCode:
            DEFAULT: int = 0x00

        def set_return_code(self, code: ReturnCode) -> None:
            self._return_code = code

        def get_return_code(self) -> ReturnCode:
            return self._return_code

        def set_packet_length(self, packet_length: int = 0):
            try:
                if packet_length > self.MAX_PACKET_LENGTH:
                    raise Exception(
                        "length should not be greater than {self.MAX_PACKET_LENGTH} bytes."
                    )
                elif packet_length < self.HEADER_SIZE:
                    raise Exception("length should be less than HEADER_SIZE.")
            except Exception as e:
                print(e)
            else:
                self._length = packet_length

        def get_length(self) -> int:
            return self._length

        def __init__(self) -> None:
            """
            Initialize a header
            """
            # 1. MessageID [32 bit]
            msg_id = self.MessageID()
            self._msg_id = msg_id.get_msg_id()

            # 2. Length [32 bit]
            # Header size is 16 bytes
            # Max size for Payload is 3K bytes
            self._length: int = 0
            self.HEADER_SIZE = 16
            self.MAX_PAYLOAD_SIZE = 3 * (2 ** 10)
            self.MAX_PACKET_LENGTH: int = self.HEADER_SIZE + self.MAX_PAYLOAD_SIZE

            # 3. RequestID [32 bit]
            request_id = self.RequestID()
            self._request_id = request_id.get_request_id()

            # 4. Protocol Version [8 bit]
            self._protocol_version: int = self.ProtocolVersion.DEFAULT

            # 5. Interface Version [8 bit]
            self._protocol_version: int = self.InterfaceVersion.DEFAULT

            # 6. Message Type [8] bit]
            self._message_type: int = None

            # 7. Return Code [8 bit]
            self._return_code: int = None

    def __init__(self) -> None:
        """
        Initialize a packet
        """
        self._header = self.Header()

        # 8. Payload [Variable size is up to 3K]
        self._payload: bytearray = None

    def get_header(self) -> Header:
        return self._header

    def get_payload(self) -> int:
        return self._payload

    def set_payload(self, payload) -> None:
        self._payload = payload


class Sender:
    def __init__(self) -> None:
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender_socket.connect(("localhost", 5004))
        # self.file = open("sent_packet.txt", "ab")

    def close(self) -> None:
        # self.file.close()
        self.sender_socket.close()

    # def save_in_file(self, packet_bytes: bytes) -> None:
    #     self.file.write(packet_bytes)

    def packet_to_bytes(self, packet: MyPacket) -> bytes:
        length = packet.get_header().get_length()
        payoad = packet.get_payload()

        # Message ID
        service_id, method_id = packet.get_header().MessageID().get_msg_id()
        packet_bytes = service_id.to_bytes(2, "big")
        packet_bytes += method_id.to_bytes(2, "big")

        # Length
        packet_bytes += length.to_bytes(4, "big")

        # Request ID
        client_id, session_id = packet.get_header().RequestID().get_request_id()
        packet_bytes += client_id.to_bytes(2, "big")
        packet_bytes += session_id.to_bytes(2, "big")

        # Protocol version
        protocol_version = packet.get_header().ProtocolVersion.DEFAULT
        packet_bytes += protocol_version.to_bytes(1, "big")

        # Interface version
        interface_version = packet.get_header().InterfaceVersion.DEFAULT
        packet_bytes += interface_version.to_bytes(1, "big")

        # Message type
        message_type = packet.get_header().MessageType.RESPONSE
        packet_bytes += message_type.to_bytes(1, "big")

        # Return code
        return_code = packet.get_header().ReturnCode.DEFAULT
        packet_bytes += return_code.to_bytes(1, "big")

        # Payload
        packet_bytes += payoad

        print(f"will send, service_id: {service_id}")
        print(f"will send, method_id: {method_id}")
        print(f"will send, length: {length}")
        print(f"will send, client_id: {client_id}")
        print(f"will send, session_id: {session_id}")
        print(f"will send, protocol: {protocol_version}")
        print(f"will send, interface: {interface_version}")
        print(f"will send, msg type: {message_type}")
        print(f"will send, return code: {return_code}")

        return packet_bytes

    def send(self, packet: MyPacket) -> None:
        packet_bytes = self.packet_to_bytes(packet)
        sent_size = self.sender_socket.send(packet_bytes)
        print(f"sent_size: {sent_size}")
        # self.save_in_file(packet_bytes)

    def receive(self) -> bool:
        header_bytes = self.sender_socket.recv(16)
        if not header_bytes:
            return False

        header = int.from_bytes(header_bytes, "big")
        service_id = header >> 14 * 8 & 0xFFFF
        method_id = header >> 12 * 8 & 0xFFFF
        length = header >> 8 * 8 & 0xFFFFFFFF
        client_id = header >> 6 * 8 & 0xFFFF
        session_id = header >> 4 * 8 & 0xFFFF
        protocol_version = header >> 3 * 8 & 0xFF
        interface_version = header >> 2 * 8 & 0xFF
        message_type = header >> 1 * 8 & 0xFF
        return_code = header & 0xFF

        print(f"received, service_id: {service_id}")
        print(f"received, method_id: {method_id}")
        print(f"received, length: {length}")
        print(f"received, client_id: {client_id}")
        print(f"received, session_id: {session_id}")
        print(f"received, protocol: {protocol_version}")
        print(f"received, interface: {interface_version}")
        print(f"received, msg type: {message_type}")
        print(f"received, return code: {return_code}")

        # Payload
        payload = self.sender_socket.recv(length - 16)

        self.header = header
        self.payload = payload

        return True


class PacketSize:
    HEADER_16: int = 16
    MAX_PAYLOAD_3K: int = 3 * (2 ** 10)
    MAX: int = HEADER_16 + MAX_PAYLOAD_3K


def make_random_data(payload_length: int) -> List[int]:
    """
    Generate random data for payload
    """
    payload = bytearray(payload_length)

    for index in range(payload_length):
        data = random.randint(0, 255)  # 1 byte for data
        payload[index] = data

    return payload


def get_random_payload_size() -> int:
    """
    Generate a random number for the size of the payload
    """
    return random.randint(0, PacketSize.MAX_PAYLOAD_3K)


def settings_for_packet(packet: MyPacket) -> None:
    """
    settings for a packet
    """
    header = packet.get_header()

    # 1. Length
    payload_length: int = get_random_payload_size()
    header.set_packet_length(PacketSize.HEADER_16 + payload_length)

    # 2. Message Type
    header.set_message_type(header.MessageType.RESPONSE)

    # 3. Payload
    packet.set_payload(make_random_data(payload_length))


def main():
    packet = MyPacket()
    sender = Sender()

    # for _ in range(2):
    while True:
        settings_for_packet(packet)
        sender.send(packet)
        print("#################################################")
        sender.receive()
        print("#################################################")
        time.sleep(1)

    sender.close()


if __name__ == "__main__":
    main()
