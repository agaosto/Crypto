import hashlib
import json
import TransactionData as td


class CoolCoinBlock:

    def __init__(self, index,prev_hash, data:td.TransactionData):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data #json

    def calculate_hash(self):
        block_of_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_of_string.encode()).hexdigest()
    def get_data(self):
        return self.data
    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)
