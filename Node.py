from RewardData import RewardData
import hashlib
import json
from RsaOperations import RsaOperations
class Node:
    def __init__(self, user )-> None:
        self.user = user
        self.visited= False
        self.blockchain = []
        self.pending_transactions = []
        self.head_hash = 0
        pass
    def add_transaction_to_pending(self, recipient, coin: list):
        transaction_data = self.user.request_transaction(recipient, coin)
        self.pending_transactions.append(transaction_data)
        pass
    def get_pending_transaction(self):
        return self.pending_transactions[0]
    def set_node_as_visited(self):
        self.visited = True
    def get_visited(self):
        return self.visited
    def clear_pending_transactions(self):
        self.pending_transactions = []
    def add_reward_to_pending(self, reward_data:RewardData):
        self.pending_transactions.append(reward_data)
    def add_pending_transactions_to_blockchain(self):
        self.blockchain.append(self.pending_transactions)
    def proof_of_work(self,max_nonce, difficulty_bits):
        target = 2 ** (256-difficulty_bits)
        header = self.head_hash
        for nonce in range(max_nonce):
            hash_result = hashlib.sha256((str(header)+str(nonce)).encode()).hexdigest()
            if int(hash_result, 16) < target:
                #solved
                return True
        return False
    def calculate_hash(self) -> str:
        data_to_hash = self.get_previous_block()
        result = hashlib.sha256(data_to_hash.encode()).hexdigest()
        self.head_hash = result
        self.user.user_hash = result
        return result
    def get_previous_block(self):
        return self.blockchain[-1]
    def check_for_double_spending(self):
        public_key = self.user.public_key
        current_coins = self.checkout()
        for transaction in self.pending_transactions:
                if(transaction.recipient==public_key and transaction.sender!="reward"):
                    for coin in transaction.coin:
                        current_coins.append(coin)
                if(transaction.sender==public_key):
                    for coin in transaction.coin:
                        if(current_coins.count(coin)>0):
                            current_coins.remove(coin)
                        else:
                            return True
        return False
    def checkout(self):
        public_key = self.user.public_key
        coin_list = []
        for block in self.blockchain:
            loaded_data = json.loads(block)
            data_of_block = loaded_data["data"]
            for data in data_of_block:
                single_block_row = json.loads(data)  
                if(single_block_row["recipient"]==public_key and single_block_row["sender"]=="reward"):
                    for coin in single_block_row["coin"]:
                        coin_list.append(coin)
                if(single_block_row["recipient"]==public_key and single_block_row["sender"]!="reward"):
                    for coin in single_block_row["coin"]:
                        coin_list.append(coin)
                if(single_block_row["sender"]==public_key):
                    for coin in single_block_row["coin"]:
                        if(coin_list.count(coin)>0):
                            coin_list.remove(coin)
        return coin_list
    def validate_hash(self) -> bool:
        if(self.head_hash != self.user.user_hash):
            print("Wrong user's hash")
            return False
        else:
            return True
    def validate_signature(self)->bool:
        for transaction in self.pending_transactions:        
                pub = transaction.sender
                recipient = transaction.recipient
                signature = transaction.signed
                coins = transaction.coin
                if(pub=="reward"):
                    continue
                else:
                    if(not(RsaOperations.verify_signature(pub+recipient+str(coins), signature, RsaOperations.load_public_key(pub)))):
                        return False
        return True
    def validate_transaction(self):
        return self.validate_hash() and not(self.check_for_double_spending()) and self.validate_signature()
