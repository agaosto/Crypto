import hashlib


class CoolCoinBlock:

    def __init__(self, index, prev_hash, data):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data #json

    def calculate_hash(self):
        block_of_string = "{}{}{}".format(
            self.index, self.prev_hash, self.data)
        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "\nNo. of transaction: {}\nPrevious hash: {}\nData of transaction: {}\n".format(self.index, self.prev_hash, self.data)
