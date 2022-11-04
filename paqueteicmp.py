import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

ip_header  = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service | Total Length
ip_header += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
ip_header += b'\x02\x06\xa6\xec'  # TTL, Protocol | Header Checksum
ip_header += b'\xC0\xA8\x16\xB4'  # Source Address
ip_header += b'\x5b\x8e\xd6\xb5'  # Destination Address

icmp_header  = b'\x30\x39\x00\x50' # Source Port | Destination Port
icmp_header += b'\x00\x00\x00\x00' # Sequence Number
icmp_header += b'\x00\x00\x00\x00' # Acknowledgement Number
icmp_header += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags | Window Size
icmp_header += b'\x04\xa9\x00\x00' # Checksum | Urgent Pointer
packet = ip_header + icmp_header
s.sendto(packet, ('91.142.214.181', 0))
