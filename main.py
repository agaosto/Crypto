from CoinBlockChainManager import CoinBlockChainManager
from TransactionData import TransactionData
from Users import Users



def main() -> None:
    #print("Starting the chain")
    #cli = CommmandLineHandler()
    Users.add_user("john")
    Users.add_user("bob")
    Users.add_user("ann")

    list_of_users = Users.get_users_data()
    john = list_of_users[0]
    bob = list_of_users[1]
    blockchain = CoinBlockChainManager()
    blockchain.create_coin_table(5)
    blockchain.give_coins(john, 2)
    blockchain.give_coins(bob, 2)
    blockchain.initialize_first_block()
    #blockchain.perform_transaction
    #wybierz usera z tablicy
    #john.request_transaction("bob", 1, blockchain)
    transaction = TransactionData("john", "bob", 3)
    blockchain.perform_transaction(transaction)
    blockchain.show_chain()
   

if __name__ == "__main__":
    main()
