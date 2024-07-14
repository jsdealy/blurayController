#!/usr/bin/env python3
import broadlink
import pickle
from sys import argv

if len(argv) == 0:
    print("No command given.")
    exit(1)

deviceIP = ""
with open("/home/justin/.broadlinkIP") as file:
    deviceIP = file.readline()

if len(argv) >= 2 and argv[2].startswith("192.168"):
    deviceIP = argv[2]

count = 0
while True:
    try:
        if count > 5:
            print("Failed to connect to device & authorize.")
            exit(1)
        device = broadlink.hello(deviceIP)
        device.auth()
        break
    except:
        count += 1

packets = {}

try:
    with open("/home/justin/.broadlinkBlurayControllerPackets", "rb") as file:
        packets = pickle.load(file)
except:
    print("Failed to open packet dictionary from file.")
    exit(1)

try:
    device.send_data(packets[argv[1]])
except:
    print("Failed to send data.")
    exit(1)
