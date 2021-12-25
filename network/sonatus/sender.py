# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
Client
"""
from typing import List, Tuple
from enum import IntEnum
import random
import sys


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
            class ServiceID(IntEnum):
                """
                2 bytes
                """

                DEFAULT: int = 0x1001

            class MethodID(IntEnum):
                """
                2 bytes
                """

                DEFAULT: int = 0x2001

            def __init__(
                self,
                service_id: int = ServiceID.DEFAULT,
                method_id: int = MethodID.DEFAULT,
            ) -> None:
                self._msg_id: Tuple[int, int] = (service_id, method_id)

            def get_msg_id(self) -> Tuple[int, int]:
                return self._msg_id

        class RequestID:
            class ClientID(IntEnum):
                """
                2 bytes
                """

                DEFAULT: int = 0x3001

            class SessionID(IntEnum):
                """
                2 bytes
                """

                DEFAULT: int = 0x4001

            def __init__(
                self,
                client_id: int = ClientID.DEFAULT,
                session_id: int = SessionID.DEFAULT,
            ) -> None:
                self._request_id: Tuple[int, int] = (client_id, session_id)

            def get_request_id(self) -> Tuple[int, int]:
                return self._request_id

        class ProtocolVersion(IntEnum):
            DEFAULT: int = 0x01

        class InterfaceVersion(IntEnum):
            DEFAULT: int = 0x01

        class MessageType(IntEnum):
            REQUEST: int = 0x00
            RESPONSE: int = 0x80

        def set_message_type(self, type: MessageType):
            self._message_type = type

        def get_message_type(self) -> MessageType:
            return self._message_type

        class ReturnCode(IntEnum):
            DEFAULT: int = 0x00

        def set_return_code(self, code: ReturnCode) -> None:
            self._return_code = code

        def get_return_code(self) -> ReturnCode:
            return self._return_code

        def set_length(self, length: int = 0):
            try:
                if length > self.MAX_LENGTH:
                    raise Exception(
                        "length should not be greater than {self.MAX_LENGTH} bytes."
                    )
                elif length < 0:
                    raise Exception("length should be less than 0.")
            except Exception as e:
                print(e)
            else:
                self._length = length

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
            self.MAX_LENGTH: int = self.HEADER_SIZE + self.MAX_PAYLOAD_SIZE

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
        self._payload: List[int] = None

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
        pass

    def send(self, packet: MyPacket) -> None:
        pass

    def receive(self) -> MyPacket:
        pass


class PacketSize(IntEnum):
    HEADER_16: int = 16
    MAX_PAYLOAD_3K: int = 3 * (2 ** 10)
    MAX: int = HEADER_16 + MAX_PAYLOAD_3K


def make_random_data(length: int) -> List[int]:
    payload: List[int] = []

    for _ in range(length):
        data = random.randint(0, 256)  # 1 byte for data
        payload.append(data)

    return payload


def get_random_payload_size() -> int:
    return random.randint(PacketSize.HEADER_16, PacketSize.MAX + 1)


def make_packet_for_sending(packet: MyPacket) -> None:
    header = packet.get_header()
    payload = packet.get_payload()

    # 1. Length
    payload_length: int = get_random_payload_size()
    print(f"payload_length = {payload_length}")
    header.set_length(PacketSize.HEADER_16 + payload_length)

    # 2. Message Type
    header.set_message_type(header.MessageType.RESPONSE)

    # 3. Payload
    packet.set_payload(make_random_data(payload_length))


def receive() -> MyPacket:
    packet = MyPacket()
    header = packet.get_header()
    payload = packet.get_payload()

    # 1. Length
    header.set_length(get_random_length())

    # 2. Message Type
    header.set_message_type(header.MessageType.RESPONSE)

    # 3. Return Code
    # header(16) + "Hello"(5)
    header.set_length(21)


def main():
    """
    1. set a random number for lenth(Header + Payload), Max payload is 3K
    """
    packet = MyPacket()
    make_packet_for_sending(packet)
    print(f"sys.getsizeof(packet) = {sys.getsizeof(packet)}")
    print(f"sys.getsizeof(packet._header) = {sys.getsizeof(packet._header)}")
    print(f"packet._header.get_length() = {packet._header.get_length()}")
    print(f"sys.getsizeof(packet._payload) = {sys.getsizeof(packet._payload)}")
    print(f"List[int] = {sys.getsizeof(List[int])}")


if __name__ == "__main__":
    main()
