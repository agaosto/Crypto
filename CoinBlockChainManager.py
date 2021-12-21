import hashlib

from CoolCoinBlock import CoolCoinBlock
from Coin import Coin
from TransactionData import TransactionData
import Users as us
import json
from RsaOperations import RsaOperations


class ConblockChainManagerSingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CoinBlockChainManager(metaclass=ConblockChainManagerSingletonMeta):

    def __init__(self) -> None:
        self.chain = []
        self.current_data = []
        self.coin_table = []
        self.genesis_data = []
        self.head_hash = 0
        self.public_key, self.private_key = RsaOperations.generate_pair_of_keys()

    def create_coin_table(self, number_of_coins) -> None:
        for i in range(0, number_of_coins):
            coin = Coin(
                id = i
            )
            self.coin_table.append(coin)
        pass

    def give_coins(self, user: us.User, number_of_coins) -> None:
        temp_coin_id_table = []
        for i in range(0, number_of_coins):
            temp_coin_id_table.append(self.coin_table.pop(0).id)
        message = "{\"create\": " +json.dumps(temp_coin_id_table)+", \"recipent\": " +json.dumps(user.public_key)
        signature = ", \"signed\": "+json.dumps(RsaOperations.generate_sign(json.dumps(str(temp_coin_id_table)+user.public_key), RsaOperations.load_private_key(self.private_key)).decode('ascii'))+"}"
        self.genesis_data.append(message+signature)

    def validate_blockchain(self) -> str:
        return self.calculate_hash(self.get_previous_block())

    def calculate_hash(self, block: CoolCoinBlock) -> str:
        block_of_string = json.dumps(block.__dict__, sort_keys = True)
        result = hashlib.sha256(block_of_string.encode()).hexdigest()
        return result
    def validate_coins_signature(self, user: us.User) -> bool:
            coins = self.get_user_coins(user.public_key)
            message = json.dumps(str(coins)+user.public_key)
            return RsaOperations.verify_signature(message, self.get_genesis_signature(user.public_key), RsaOperations.load_public_key(self.public_key))
        
    def initialize_genesis_block(self) -> None:
        for elem in self.genesis_data:
            self.current_data.append(elem)
        self.construct_block(self.head_hash)
        us.Users.update_hash(self.head_hash)

    def construct_block(self, hash) -> CoolCoinBlock:
        block = CoolCoinBlock(
            index = len(self.chain),
            data = self.current_data,
            prev_hash = hash,

        )
        self.current_data = []
        self.chain.append(block)
        self.head_hash = self.calculate_hash(block)
        return block

    def get_previous_block(self) -> CoolCoinBlock:
        return self.chain[-1]

    def add_new_data(self, transaction_data: str) -> bool:
        self.current_data.append(transaction_data)
        return True

    def perform_transaction(self, transaction_data: TransactionData) -> None:

        if(self.validate_transaction(transaction_data)):
            previous_block = self.get_previous_block()
            self.add_new_data(transaction_data.get_json_of_transaction())
            previous_hash = self.calculate_hash(previous_block)
            self.construct_block(previous_hash)
            us.Users.update_hash(self.head_hash)
        else:
            pass

    def show_chain(self) -> None:
        print(self.chain)
        pass
    def get_genesis_signature(self, user: us.User):
        data = self.get_genesis_block().get_data()
        for elem_json in data:
            elem = json.loads(elem_json)
            if(elem["recipent"] == user):
                return elem["signed"]
        print("Error: No such user")
        pass
    def get_user_coins(self, user) -> list:
        data = self.get_genesis_block().get_data()
        for elem_json in data:
            elem = json.loads(elem_json)
            if(elem["recipent"] == user):
                return elem["create"]
        print("Error: No such user")
        pass

    def get_genesis_block(self) -> CoolCoinBlock:
        return self.chain[0]

    def get_length_of_chain(self) -> int:
        return self.chain.__len__()

    def get_available_coins(self, user) -> list:
        user_coins = self.get_user_coins(user)
        for i in range(1, self.get_length_of_chain()):
            transaction = json.loads(self.chain[i].get_data()[0])
            sender = transaction["sender"]
            recipent = transaction["recipient"]
            coin_id = transaction["coin"]
            for coin in coin_id:
                if(transaction["sender"] != user and transaction["recipient"] != user):
                    continue
                elif(transaction["sender"] == user and user_coins.count(coin) > 0):
                    user_coins.remove(coin)
                if(transaction["recipient"] == user):
                    user_coins.append(coin)
        return user_coins

    def validate_coins(self, transaction_data: TransactionData) -> bool:
        available_coins = self.get_available_coins(
            transaction_data.sender)
        for coin in transaction_data.coin:
            if(available_coins.count(coin) == 0):
                print("Error: " + us.Users.get_user_by_public_key(transaction_data.sender).name +
                      ", you're trying to use coin(s) you don't have")
                return False
        else:
            return True

    def validate_hash(self, transaction_data: TransactionData) -> bool:
        if(self.head_hash != us.Users.get_user_by_public_key(transaction_data.sender).user_hash):
            print("Wrong user's hash")
            return False
        else:
            return True
    def validate_signature(self, transaction_data: TransactionData)->bool:
        pub = transaction_data.sender
        signature = transaction_data.signed
        return RsaOperations.verify_signature(pub+transaction_data.recipient+str(transaction_data.coin), signature, RsaOperations.load_public_key(pub))

    def validate_transaction(self, transaction_data: TransactionData) -> bool:
        if(self.validate_coins(transaction_data) and self.validate_hash(transaction_data) and self.validate_signature(transaction_data)):
            print(us.Users.get_user_by_public_key(transaction_data.sender).name+ "'s transaction successful")
            return True
        else:
            print(us.Users.get_user_by_public_key(transaction_data.sender).name + "'s transaction is invalid!")
            return False
