#!/usr/bin/env python3
import broadlink
import pickle

deviceIP = "192.168.1.139"
while True:
    try:
        device = broadlink.hello(deviceIP)
        print(f"Device found: {device}")
        device.auth()
        break
    except:
        deviceIP = input("What's the broadlink local IP: ")

packets = {
    "menu": b'x00',
    "back": b'x00',
    "okay": b'x00',
    "up": b'x00',
    "down": b'x00',
    "left": b'x00',
    "right": b'x00',
    "play": b'x00',
    "pause": b'x00',
    "stop": b'x00',
    "fastforward": b'x00',
    "rewind": b'x00',
    "eject": b'x00',
    "bluraypower": b'x00',
    "tvpower": b'x00',
}

try:
    with open("/home/justin/.broadlinkBlurayControllerPackets", "wb") as file:
        for name in packets:
            count = 0
            while True:
                if count > 5:
                    print("Quitting...")
                    exit(1)
                try:
                    device.enter_learning()
                    thing = input(f"Send {name} button, then press any key.")
                    packets[name] = device.check_data()
                    print(f"\nPacket determined: {packets[name]}\n")
                    break
                except: 
                    print("Let's try that again...")
                    count += 1
        pickle.dump(packets, file)
        print(f"Success. Here's the data that was saved: {packets}")

except:
    print("Failed to open the /home/justin/.broadlinkBlurayControllerPackets file!")

