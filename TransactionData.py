import json
from Users import User
from RsaOperations import RsaOperations


class TransactionData:

    def __init__(self, sender: User, recipient: str, coin: list) -> None:
        self.sender = sender.public_key
        self.recipient = recipient
        self.coin = coin
        self.sign = (RsaOperations.generate_sign("test", RsaOperations.load_private_key(sender.private_key))).decode('ascii')
        pass

    def get_json_of_transaction(self) -> str:
        return json.dumps(self.__dict__,  default=lambda o: o.encode())
