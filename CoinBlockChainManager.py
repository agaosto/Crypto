from array import array
import hashlib
from CoolCoinBlock import CoolCoinBlock
from Coin import Coin
from TransactionData import TransactionData
import Users as us
import json

class ConblockChainManagerSingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CoinBlockChainManager(metaclass=ConblockChainManagerSingletonMeta):

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.coin_table = []
        self.genesis_data = []
        self.head_hash = 0

    def create_coin_table(self, number_of_coins):
        for i in range(0, number_of_coins):
            coin = Coin(
                id = i
            )
            self.coin_table.append(coin)
        pass

    def give_coins(self, user: us.User, number_of_coins):
        temp_coin_id_table = []
        for i in range(0, number_of_coins):
            temp_coin_id_table.append(self.coin_table.pop(0).id)
        message = "{\"create\": " +json.dumps(temp_coin_id_table)+", \"recipent\": \"" +user.name+"\"}"
        self.genesis_data.append(message)

    def validate_blockchain(self)->str:
        return self.calculate_hash(self.get_previous_block())

    def calculate_hash(self, block: CoolCoinBlock):
        block_of_string = json.dumps(block.__dict__, sort_keys=True)
        result = hashlib.sha256(block_of_string.encode()).hexdigest()
        return result
        
        
    def initialize_first_block(self):
        for elem in self.genesis_data:
            self.current_data.append(elem)
        self.construct_block(self.head_hash)
        us.Users.update_hash(self.head_hash)

    def construct_block(self, hash):
        block = CoolCoinBlock(
            index=len(self.chain),
            data=self.current_data,
            prev_hash=hash
        )
        self.current_data = []
        self.chain.append(block)
        self.head_hash = self.calculate_hash(block)

        return block


    def get_previous_block(self):
        return self.chain[-1]

    def add_new_data(self, transaction_data: str):
        # adds a new transaction to the data of the transactions
        self.current_data.append(transaction_data)
            #f"{transaction_data.sender} PAYS {transaction_data.coin} TO {transaction_data.recipent}"
        return True

    def perform_transaction(self, transaction_data: TransactionData) -> None:
        
        if(self.validate_transaction(transaction_data)):
            previous_block = self.get_previous_block()
            self.add_new_data(transaction_data.get_json_of_transaction())
            previous_hash = self.calculate_hash(previous_block)
            # aktualizacja hasha userow
            self.construct_block(previous_hash)
            us.Users.update_hash(self.head_hash)
        else:
            pass
    def show_chain(self)->None:
        print(self.chain)
        pass
    def get_user_coins(self, user:us.User)->list:
        data = self.get_genesis_block().get_data()
        for elem_json in data:
            elem = json.loads(elem_json)
            if(elem["recipent"] == user):
                 return elem["create"]
            else:
                print("No such user")
                pass
    def get_genesis_block(self):
        return self.chain[0]
    def get_length_of_chain(self):
        return self.chain.__len__()
    def get_available_coins(self, user:str)->list:
        user_coins = self.get_user_coins(user)
        for i in range(1, self.get_length_of_chain()):
            transaction = json.loads(self.chain[i].get_data()[0])
            print(transaction["coin"])
            sender = transaction["sender"]
            coin_id = transaction["coin"]
            if(transaction["sender"]["name"]==user and user_coins.count(coin_id)>0):
                print("a")
                user_coins.remove(coin_id)
            #elif(user_coins.count(coin_id)==0):
                #return False
        return user_coins
    def validate_coins(self, transaction_data:TransactionData):
        available_coins = self.get_available_coins(transaction_data.sender.name)
        if(available_coins.count(transaction_data.coin)==0):
            print("error: Trying to use coin you don't have")
            return False
        else:
            return True
    def validate_hash(self, transaction_data:TransactionData)->bool:
        if(self.head_hash!=transaction_data.sender.user_hash):
            print("Wrong user hash")
            return False
        else:
            return True
    def validate_transaction(self, transaction_data:TransactionData)->bool:
        if(self.validate_coins(transaction_data) and self.validate_hash(transaction_data)):
            print("Transaction successfull")
            return True
        else:
            print("Wrong Transaction")
            return False


   