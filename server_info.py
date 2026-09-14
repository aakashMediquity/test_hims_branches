import socket
import platform
import os

print("===== SERVER INFORMATION =====")

print("Hostname :", socket.gethostname())
print("OS       :", platform.system())
print("Release  :", platform.release())
print("Machine  :", platform.machine())
print("CPU      :", os.cpu_count())

print("==============================")