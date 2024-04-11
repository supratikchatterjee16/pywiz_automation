import time
import asyncio
from pywizlight import wizlight, PilotBuilder

# Some basics
pilot_sets = {
	"white" : PilotBuilder(rgb=(255, 255, 255), brightness=255),
	"teal" : PilotBuilder(rgb=(0, 255, 255), brightness=255),
	"red" : PilotBuilder(rgb=(255, 0, 0), brightness=255),
	"purple" : PilotBuilder(rgb=(255, 0, 255), brightness=255),
	"teal_dim" : PilotBuilder(rgb=(0, 255, 255), brightness=10)
	}

profiles = [
	["red", "purple", "teal"],
	["purple", "teal", "white"]
]

bulb_ips = ["192.168.1.6"]

# Function to set value of all bulbs
async def set_bulbs(pilot):
	global bulb_ips
	for ip in bulb_ips:
		light = wizlight(ip)
		await light.turn_on(pilot)

from .functions import *

# Main function
def run(func, delay = 1):
	loop = asyncio.get_event_loop()
	while True:
		pilot = func()
		loop.run_until_complete(set_bulbs(pilot))
		print(pilot.__dict__)
		time.sleep(delay)

#run()
# nmap -sV --allports -T4 192.168.1.0/24
