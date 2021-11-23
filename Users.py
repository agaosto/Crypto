
import CoinBlockChainManager
import TransactionData as ts
import json
class Users:
    users = []

    def add_user(name):
        user = User(
            name=name
        )
        Users.users.append(user)
        pass

    def get_users_count() -> int:
        return len(Users.users)

    def get_users_data():
        return Users.users

    def update_hash(hash) -> None:
        for user in Users.users:
            user.user_hash = hash
        pass


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.user_hash = 0
        pass

    def validate_blockchain(self, blockchain: CoinBlockChainManager):
        if(blockchain.validate_blockchain()==self.user_hash):
            print("OK")
        else:
            print("WRONG")
        pass

    def checkout(self, blockchain: CoinBlockChainManager):

        print(self.name+" your coins: "+str(blockchain.get_available_coins(self.name)))
        pass
    def get_user_hash(self):
        return self.user_hash
    def request_transaction(self, recipient, coin, blockchain: CoinBlockChainManager):
        transaction = ts.TransactionData(self, recipient, coin)
        blockchain.perform_transaction(transaction)
        pass
    def encode(self):
        return self.__dict__