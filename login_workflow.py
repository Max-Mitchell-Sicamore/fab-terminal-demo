from novunex_networking import user,requester

class UserLoginWorkFLow:

    def __init__(self,rf_id):
        self.rf_id = rf_id

    def run(self):
        return user.User.init_using_rfid_card(
            requester.GetRequester(False),
            self.rf_id
        ).get_full_name()
