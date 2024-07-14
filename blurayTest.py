#!/usr/bin/env python3
import broadlink
import pickle
from sys import argv

deviceIP = argv[1]
try:
    device = broadlink.hello(deviceIP,broadlink.DEFAULT_PORT,3)
    print(f"Device found: {device}")
except:
    print("Device not found.")
