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

# from struct import *
import socket


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

    def read(self) -> None:
        """
        1. Read 4 bytes for Message ID
        2. Read 4 bytes for Length
        3. Read 4 bytes for Request ID
        4. Read 1 byte for Protocol Version
        5. Read 1 byte for Interface Version
        6. Read 1 byte for Message Type
        7. Read 1 byte for Return Code
        8. Read (Length size - Header size) bytes for Payload
        """

    def send(self) -> None:
        pass

    def receive(self) -> None:
        pass


class Sender:
    def __init__(self) -> None:
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.connect(("localhost", 5004))

    def send(self, packet: MyPacket) -> None:
        length = packet.get_header().get_length()
        payoad = packet.get_payload()

        # Message ID
        service_id, method_id = packet.get_header().MessageID().get_msg_id()
        sent_size = self.tcp_socket.send(service_id.to_bytes(2, "big"))
        sent_size = self.tcp_socket.send(method_id.to_bytes(2, "big"))

        # Length
        sent_size = self.tcp_socket.send(length.to_bytes(4, "big"))

        # Request ID
        client_id, session_id = packet.get_header().RequestID().get_request_id()
        sent_size = self.tcp_socket.send(client_id.to_bytes(2, "big"))
        sent_size = self.tcp_socket.send(session_id.to_bytes(2, "big"))

        # Protocol version
        protocol_version = packet.get_header().ProtocolVersion.DEFAULT
        sent_size = self.tcp_socket.send(protocol_version.to_bytes(1, "big"))

        # Interface version
        interface_version = packet.get_header().InterfaceVersion.DEFAULT
        sent_size = self.tcp_socket.send(interface_version.to_bytes(1, "big"))

        # Message type
        message_type = packet.get_header().MessageType.RESPONSE
        sent_size = self.tcp_socket.send(message_type.to_bytes(1, "big"))

        # Return code
        return_code = packet.get_header().ReturnCode.DEFAULT
        sent_size = self.tcp_socket.send(return_code.to_bytes(1, "big"))

        print(f"service_id: {service_id}")
        print(f"method_id: {method_id}")
        print(f"length: {length}")
        print(f"client_id: {client_id}")
        print(f"session_id: {session_id}")
        print(f"protocol: {protocol_version}")
        print(f"interface: {interface_version}")
        print(f"msg type: {message_type}")
        print(f"return code: {return_code}")

    def receive(self) -> MyPacket:
        pass


class PacketSize:
    HEADER_16: int = 16
    MAX_PAYLOAD_3K: int = 3 * (2 ** 10)
    MAX: int = HEADER_16 + MAX_PAYLOAD_3K


def make_random_data(payload_length: int) -> List[int]:
    payload = bytearray(payload_length)
    print(f"sys.getsizeof(payload): {sys.getsizeof(payload)}")

    for index in range(payload_length):
        data = random.randint(0, 255)  # 1 byte for data
        payload[index] = data

    return payload


def get_random_payload_size() -> int:
    return random.randint(0, PacketSize.MAX_PAYLOAD_3K)


def make_packet_for_sending(packet: MyPacket) -> None:
    header = packet.get_header()
    payload: bytearray = packet.get_payload()

    # 1. Length
    payload_length: int = get_random_payload_size()
    print(f"payload_length = {payload_length}")
    header.set_packet_length(PacketSize.HEADER_16 + payload_length)

    # 2. Message Type
    header.set_message_type(header.MessageType.RESPONSE)

    # 3. Payload
    packet.set_payload(make_random_data(payload_length))


def main():
    """
    1. set a random number for lenth(Header + Payload), Max payload is 3K
    """
    packet = MyPacket()
    sender = Sender()

    for _ in range(10):
        make_packet_for_sending(packet)
        sender.send(packet)

    print("finished!")
    print("check the file!")


if __name__ == "__main__":
    main()
