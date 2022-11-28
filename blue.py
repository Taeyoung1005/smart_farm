# from bluetooth import *

# client_socket = BluetoothSocket(RFCOMM)
# client_socket.connect(("98:DA:60:05:83:C3", 1))

from serial import Serial

arduino = Serial(
    port='/dev/rfcomm0',   # Window
    baudrate=115200, # 보드 레이트 (통신 속도)
    timeout=1
)

while True:
    if arduino.readable():
        msg = input("Send: ")
        if msg == "close":
            break
        arduino.write(msg.encode())

print("Finished")