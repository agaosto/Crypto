from array import array
from CoolCoinBlock import CoolCoinBlock
from Coin import Coin
from TransactionData import TransactionData
import Users as us
import json


class CoinBlockChainManager:

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

    def initialize_first_block(self):
        for elem in self.genesis_data:
            self.current_data.append(elem)
        self.construct_block(self.head_hash)

    def construct_block(self, hash):
        block = CoolCoinBlock(
            index=len(self.chain),
            data=self.current_data,
            prev_hash=hash
        )
        self.current_data = []
        self.chain.append(block)
        self.head_hash = block.calculate_hash()
        return block

    @staticmethod
    def check_validity(block, prev_block):
        print(
            f"For transaction {prev_block.index}. hash is: {prev_block.calculate_hash()}")
        print(
            f"For transaction {block.index}. previous hash is: {block.prev_hash}")
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash() != block.prev_hash:
            return False

        return True

    def get_previous_block(self):
        return self.chain[-1]

    def add_new_data(self, transaction_data: str):
        # adds a new transaction to the data of the transactions
        self.current_data.append(transaction_data)
            #f"{transaction_data.sender} PAYS {transaction_data.coin} TO {transaction_data.recipent}"
        return True

    def perform_transaction(self, transaction_data: TransactionData) -> None:
        previous_block = self.get_previous_block()
        self.add_new_data(transaction_data.get_json_of_transaction())
        last_hash = previous_block.calculate_hash()
        # aktualizacja hasha userow
        us.Users.update_hash(last_hash)
        block = self.construct_block(last_hash)
        #print("Checking if transaction is valid...")
       # if(CoolCoinBlockChain.check_validity(block, previous_block)):
        #  print("Transaction is valid, saved!")
        # else:
        #  print("Invalid transaction!")
        return True
    def show_chain(self)->None:
        print(self.chain)
        data = self.chain[0]
        test = data.get_data()
        print(test[0])
        test1 = json.loads(test[0])
        print(test1["create"]) #[0,1] mamy coiny
  
        pass
   