# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# SOME/IP Protocol Specification

from typing import List, Tuple


class PacketForSOMEoverIP:
    """
    AUTOSAR Protocol 'Scalable service-Oriented MiddlewarE over IP(SOME/IP)'

    <<--------------------------------32 bit---------------------------------->>
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
