import array
import json

from Users import User


class TransactionData:
    def __init__(self, sender:User, recipient:str, coin: array) -> None:
        self.sender = sender
        self.recipient = recipient
        self.coin = coin
        pass

    def get_json_of_transaction(self) -> str:
        return json.dumps(self.__dict__,  default=lambda o: o.encode())