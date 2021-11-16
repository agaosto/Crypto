from CoolCoinBlock import CoolCoinBlock
from Coin import Coin
import Users
import json

class CoinBlockChainManager:

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.coin_table=[]
        self.create_coin_table()
        self.initialize_first_block()

    def create_coin_table(self):
        size_of_table = Users.Users.get_users_count()
        for i in range(0, size_of_table):
            coin = Coin(
                id=i
            )
            self.coin_table.append(coin)
        pass
    
    def give_coins(self)->str:
        #'CREATE <COINID> TO USER'
        user_coins = []
        for user, coin in zip(Users.Users.get_users_data(), self.coin_table):
            message = f"CREATE {coin.id} TO {user.name}"
            user_coins.append(message)
        user_coins_json = json.dumps(user_coins)
        return user_coins_json

    def initialize_first_block(self):
        genesis_data = self.give_coins()
        self.current_data.append(
            genesis_data
        )
        self.construct_block(prev_hash=0)
        print(self.chain)

    def construct_block(self, prev_hash):
        block = CoolCoinBlock(
            index=len(self.chain),
            prev_hash=prev_hash,
            data=self.current_data
        )
        self.current_data = []
        self.chain.append(block)
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

    def add_new_data(self, sender, recipient, coin_id):
        # adds a new transaction to the data of the transactions
        self.current_data.append({
            f"{sender} PAYS {coin_id} TO {recipient}"
        })
        return True

    def perform_transaction(self, sender: str, recipent: str, coin_id:int) -> None:
        previous_block = self.get_previous_block()
        self.add_new_data(
            sender=sender,
            recipient=recipent,
            coin_id=coin_id

        )
        last_hash = previous_block.calculate_hash()
        #aktualizacja hasha userow
        Users.Users.update_hash(last_hash)
        block = self.construct_block(last_hash)
        #print("Checking if transaction is valid...")
       # if(CoolCoinBlockChain.check_validity(block, previous_block)):
          #  print("Transaction is valid, saved!")
        #else:
          #  print("Invalid transaction!")
        return True