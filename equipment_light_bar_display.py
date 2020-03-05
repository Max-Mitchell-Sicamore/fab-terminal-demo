from novunex_networking import equipment, requester
from light_bar_client import LightBarClient


class EquipmentLightBarDisplay:
    GREEN = 0,255,0
    BLUE = 0,0,255
    RED = 255,0,0
    PURPLE =  180,30,160
    GET_REQUESTER = requester.GetRequester(False)
    STATUS_LIGHTS = {
        "Ready to Use" : [GREEN,"solid"],
        "Do Not Use" : [RED,"solid"],
        "In Service" : [BLUE,"solid"],
        "Temporarily Removed" : [PURPLE,"soild"],
        "Record Approved" : [GREEN,"solid"]
    }

    def __init__(self,size):
        self.light_bar = LightBarClient(size,)

    def display_equip_status(self,segment,equip_numb):
        return self.light_bar.set_and_display_segment(
            segment,
            *self.STATUS_LIGHTS[self._get_equip_status(equip_numb)]
        )

    def _get_equip_status(self,equip_numb):
        return equipment.Equipment(
            self.GET_REQUESTER,
            equip_numb,
            "EquipmentNumber"
        ).get_status()
