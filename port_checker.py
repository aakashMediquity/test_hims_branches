import socket

ports = [
    2010, 2020, 2030, 2040, 2050,
    4010, 4020, 4030, 4040, 4050,
    4060, 4070, 4080, 4090,
    7010, 7020, 7030, 7040, 7050,
    7060, 7070, 7080, 7090, 7100,
    7200, 7500, 4444, 3100, 1100,
    5432, 6100, 5100, 9990, 9091,
    2031, 1300, 8152, 1800, 1200,
    8762, 8150, 8761, 8751, 8151,
    2100, 8100, 8101, 9200, 7300,
    7400, 8081, 4095, 4099, 4098,
    4096, 4100, 7800, 4000, 4200,
    9400, 9300
]
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)

    result = sock.connect_ex(("127.0.0.1", port))

    if result == 0:
        print(f"{port} - IN USE")
    else:
        print(f"{port} - AVAILABLE")

    sock.close()