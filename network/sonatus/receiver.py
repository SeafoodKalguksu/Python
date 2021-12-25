# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import socket
from sender import MyPacket

"""
Server
"""


class Receiver:
    pass


def receive(conn: socket, file) -> bool:
    """
    1. Header 16 bytes 한 번에 수신
    2. 헤더 파싱
    3. payload 한 번에 수신
    """
    # Message ID
    service_id = conn.recv(2)
    if not service_id:
        return False

    print(f"service_id: {int.from_bytes(service_id, 'little')}")
    method_id = conn.recv(2)
    print(f"method_id: {int.from_bytes(method_id, 'little')}")

    # Length
    length = conn.recv(4)
    print(f"length: {int.from_bytes(length, 'little')}")

    # Request ID
    client_id = conn.recv(2)
    print(f"client_id: {int.from_bytes(client_id, 'little')}")
    session_id = conn.recv(2)
    print(f"session_id: {int.from_bytes(session_id, 'little')}")

    # Protocol version
    protocol_version = conn.recv(1)
    print(f"protocol: {int.from_bytes(protocol_version, 'little')}")

    # Interface version
    interface_version = conn.recv(1)
    print(f"interface: {int.from_bytes(interface_version, 'little')}")

    # Message type
    message_type = conn.recv(1)
    print(f"msg type: {int.from_bytes(message_type, 'little')}")

    # Return code
    return_code = conn.recv(1)
    print(f"return code: {int.from_bytes(return_code, 'little')}")

    # Payload
    print(f"length: {int.from_bytes(length, 'little')}")
    payload = conn.recv(int.from_bytes(length, "little") - 16)

    print("#################################################")
    print("#################################################")

    save_in_file(
        service_id,
        method_id,
        length,
        client_id,
        session_id,
        protocol_version,
        interface_version,
        message_type,
        return_code,
        payload,
        file,
    )
    return True


def save_in_file(
    service_id,
    method_id,
    length,
    client_id,
    session_id,
    protocol_version,
    interface_version,
    message_type,
    return_code,
    payload,
    file,
) -> None:
    file.write(
        service_id
        + method_id
        + length
        + client_id
        + service_id
        + protocol_version
        + interface_version
        + message_type
        + return_code
        + payload
    )


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("localhost", 5004)
    my_socket.bind(address)
    my_socket.listen(1)
    connection, addr = my_socket.accept()
    file = open("received_packet.txt", "ab")
    print("Connected by", addr)

    # with connection:
    #     print("Connected by", addr)
    #     while True:
    #         data = connection.recv(1024)
    #         if not data:
    #             break
    #         connection.sendall(data)

    while True:
        if False == receive(connection, file):
            break

    file.close()
    connection.close()
    my_socket.close()


if __name__ == "__main__":
    main()
