#!/bin/env python
from time import sleep
from sys import argv

if len(argv) < 2:
    print("No argument supplied!")
    exit(1)

height = argv[1]
try:
    height = int(height)
except ValueError:
    print("Not a valid integer!")
    exit(1)

for i in range(0, height):
    spacing = ' ' * (height - i)
    count = i + i + 1
    stars = '•' * count
    print(f"{spacing}{stars}")
    sleep(0.1)
