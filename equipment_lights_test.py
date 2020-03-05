#!/usr/bin/python3

from equipment_light_bar_display import EquipmentLightBarDisplay
import time

while True:
    equip_lightbar = EquipmentLightBarDisplay(5)
    equip_lightbar.display_equip_status(0,"E0414")
    # equip_lightbar.display_equip_status(1,"E0341")
    # equip_lightbar.display_equip_status(2,"E0333")
    # equip_lightbar.display_equip_status(3,"E0413")
    # equip_lightbar.display_equip_status(4,"E0412")
    time.sleep(1)
