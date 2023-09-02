# VidStream
# vidstream

Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Florian Dedov from NeuralNine (c) 2020

## Examples of How To Use (Buggy Alpha Version)

Creating A Server

```python
from vidstream import StreamingServer
import threading

# CLEINT MACHINE IP
receiver = StreamingServer("192.168.13.20", 9999)
t = threading.Thread(target=receiver.start_server)
t.start()

while input("ServerSTOP Waiting >_") != "STOP":
    continue

receiver.stop_server()
```

Creating A Client
```python
from vidstream import ScreenShareClient
import threading

# CLEINT MACHINE IP
sender = ScreenShareClient("192.168.13.20",9999)
t = threading.Thread(target=sender.start_stream)
t.start()
 
while input("Clent Waiting >_") != "STOP":
    continue

sender.stop_stream()
```

