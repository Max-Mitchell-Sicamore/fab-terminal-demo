from novunex_networking import equipment, requester
from light_bar_client import LightBarClient


class EquipmentLightBarDisplay:
    PATH = "/tmp/pipe_sicamore_lightbar"
    GREEN = 0,0,255
    BLUE = 0,255,0
    RED = 255,0,0
    PURPLE =  180,160,30
    ORANGE = 255,0, 165 
    STATUS_LIGHTS = {
        "Ready to Use" : [GREEN,"solid"],
        "Do Not Use" : [RED,"solid"],
        "In Service" : [BLUE,"solid"],
        "Temporarily Removed" : [PURPLE,"solid"],
        "Record Approved" : [GREEN,"solid"],
        "Record Created" : [BLUE,"solid"],
        "Returned to Customer" : [PURPLE,"solid"],
        "Permanently Removed" : [ORANGE,"solid"]

    }

    def __init__(self,size,production=False):
        self.light_bar = LightBarClient(size,"fake.txt")
        self.GET_REQUESTER = requester.GetRequester(production)

    def display_equip_status(self,segment,equip_numb):
        self.light_bar.set_and_display_segment(
            segment,
            *self.STATUS_LIGHTS[self._get_equip_status(equip_numb)]
        )

    def _get_equip_status(self,equip_numb):
        return equipment.Equipment(
            self.GET_REQUESTER,
            equip_numb,
            "EquipmentNumber"
        ).get_status()
