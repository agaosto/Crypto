
import CoinBlockChainManager 
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
    def update_hash(hash)->None:
        for user in Users.users:
            user.user_hash = hash
        pass


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.user_hash = 0
        pass
    def validate_blockchain():
        pass
    def checkout():
        pass
    def request_transaction(self, recipent:str, coin_id:int, blockchain:CoinBlockChainManager):
        #blockchain = CoinBlockChainManager()
        is_done_flag = blockchain.perform_transaction(self.name, recipent, coin_id)
        if(is_done_flag): 
            print("OK")
        else:
            print("NIEOK")
        pass



