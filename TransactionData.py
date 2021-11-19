import array
import json


class TransactionData:
    def __init__(self, sender:str, recipient:str, coin: array) -> None:
        self.sender = sender
        self.recipient = recipient
        self.coin = coin
        pass

    def get_json_of_transaction(self) -> str:
        return json.dumps(self.__dict__)