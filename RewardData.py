import json
from User import User


class RewardData:
    def __init__(self, recipent: User, coin: list) -> None:
        self.sender = "reward"
        self.recipient = recipent.public_key
        self.coin = coin
        self.signed = "reward"
        pass

    def get_json_of_reward(self) -> str:
        return json.dumps(self.__dict__,  default=lambda o: o.encode())
