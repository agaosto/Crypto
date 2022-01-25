from RsaOperations import RsaOperations
import json


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.user_hash = 0
        self.public_key, self.private_key = RsaOperations.generate_pair_of_keys()
        pass

    def get_user_hash(self) -> int:
        return self.user_hash

    def request_transaction(self, recipient, coin: list):
        return TransactionData(self, recipient, coin)

    def encode(self):
        return self.__dict__


class TransactionData:
    def __init__(self, sender: User, recipient: str, coin: list) -> None:
        self.sender = sender.public_key
        self.recipient = recipient
        self.coin = coin
        self.signed = (RsaOperations.generate_sign(str(sender.public_key)+recipient+str(
            coin), RsaOperations.load_private_key(sender.private_key))).decode('ascii')
        pass

    def get_json_of_transaction(self) -> str:
        return json.dumps(self.__dict__,  default=lambda o: o.encode())
