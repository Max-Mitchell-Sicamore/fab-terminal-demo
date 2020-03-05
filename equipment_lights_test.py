#!/usr/bin/python3

from equipment_light_bar_display import EquipmentLightBarDisplay
import time

while True:
	equip_lightbar = EquipmentLightBarDisplay(5)
	equip_lightbar.display_equip_status(0,"E0414")
	time.sleep(1)
