from rsa.key import PrivateKey
import CoinBlockChainManager
import TransactionData as ts
from RsaOperations import RsaOperations

class Users:
    users = []

    def add_user(name) -> None:
        user = User(
            name = name
        )
        Users.users.append(user)
        pass

    def get_users_count() -> int:
        return len(Users.users)

    def get_users_data() -> list:
        return Users.users
    def get_user_by_public_key(pub):
        for user in Users.users:
            if(pub==user.public_key):
                return user
    def update_hash(hash) -> None:
        for user in Users.users:
            user.user_hash = hash
        pass


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.user_hash = 0
        self.public_key, self.private_key = RsaOperations.generate_pair_of_keys()
        pass

    def validate_blockchain(self, blockchain: CoinBlockChainManager) -> None:
        if(blockchain.validate_blockchain() == self.user_hash):
            print("Blockchain validated by " + self.name)
        else:
            print("Invalid blockchain! Hash stored by " +
                  self.name + " doesn't match!")
        pass
    
    def checkout(self, blockchain: CoinBlockChainManager) -> None:
        print(self.name+"'s coins: " +
              str(blockchain.get_available_coins(self.public_key)))
        pass

    def get_user_hash(self) -> int:
        return self.user_hash
    def validate_coins(self, blockchain: CoinBlockChainManager):
        if(blockchain.validate_coins_signature(self)):
            print(self.name +" coins are signed by manager")
        else:
            print(self.name +" coins are NOT signed by manager")
    def request_transaction(self, recipient, coin: list, blockchain: CoinBlockChainManager) -> None:
        transaction = ts.TransactionData(self, recipient, coin)
        blockchain.perform_transaction(transaction)
        pass

    def encode(self):
        return self.__dict__
