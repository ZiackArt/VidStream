from vidstream import ScreenShareClient
import threading

# CLEINT MACHINE IP
sender = ScreenShareClient("192.168.13.20",9999)
t = threading.Thread(target=sender.start_stream)
t.start()
 
while input("Clent Waiting >_") != "STOP":
    continue

sender.stop_stream()