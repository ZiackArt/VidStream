from vidstream import StreamingServer
import threading

# CLEINT MACHINE IP
receiver = StreamingServer("192.168.13.20", 9999)
t = threading.Thread(target=receiver.start_server)
t.start()

while input("ServerSTOP Waiting >_") != "STOP":
    continue

receiver.stop_server()