#!/usr/bin/env python3
import broadlink
import pickle
from sys import argv
from sys import exit

if len(argv) == 0:
    print("No command given.")
    exit(1)

deviceIP = ""
with open("/home/justin/.broadlinkIP") as file:
    deviceIP = file.readline()
if len(argv) >= 2 and argv[1].startswith("192.168"):
    deviceIP = argv[1]
count = 0
while True:
    if count > 5:
        print("Quitting...")
        exit(1)
    try:
        device = broadlink.hello(deviceIP)
        print(f"Device found: {device}")
        device.auth()
        break
    except:
        print("Problem connecting to device.")
        deviceIP = input("What's the broadlink local IP: ")
        count += 1

packets = {
    "yamahapower": b'x00',
    "yamahavolup": b'x00',
    "yamahavoldown": b'x00',
    "stripon": b'x00',
    "stripoff": b'x00',
    "striporange": b'x00',
    "stripblue": b'x00',
    "stripwhite": b'x00'
}

try:
    with open("/home/justin/.broadlinkFanAndLightsControllerPackets", "wb") as file:
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
    print("Failed to open the /home/justin/.broadlinkFanAndLightsControllerPackets file!")

