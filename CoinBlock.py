import json


class CoinBlock:
    def __init__(self, prev_hash, data) -> None:
        self.prev_hash = prev_hash
        self.data = data

    def get_data(self):
        return self.data

    def get_json_of_block(self):
        return json.dumps(self.__dict__, indent=4)
