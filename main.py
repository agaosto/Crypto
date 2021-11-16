#from CoinBlockChainManager import CoinBlockChainManager
from CoinBlockChainManager import CoinBlockChainManager
from Users import Users



def main() -> None:
    #print("Starting the chain")
    #cli = CommmandLineHandler()
    Users.add_user("john")
    Users.add_user("bob")
    Users.add_user("ann")
    list_of_users = Users.get_users_data()
    for i in list_of_users:
        print (i.user_hash)
    john = list_of_users[0]
    blockchain = CoinBlockChainManager()
    #blockchain.initialize_first_block()
    #wybierz usera z tablicy
    john.request_transaction("bob", 1, blockchain)

if __name__ == "__main__":
    main()
