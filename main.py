import base64
from rsa.key import PublicKey
from CoinBlockChainManager import CoinBlockChainManager
from Users import Users
import json
from RsaOperations import RsaOperations
import rsa

def main() -> None:
    # creating users
    Users.add_user("John")
    Users.add_user("Bob")
    Users.add_user("Ann")

    list_of_users = Users.get_users_data()
    john = list_of_users[0]
    bob = list_of_users[1]
    ann = list_of_users[2]

    # creating blockchain
    blockchain = CoinBlockChainManager()

    # coin distribution
    blockchain.create_coin_table(7)
    blockchain.give_coins(john, 2)
    blockchain.give_coins(bob, 2)
    blockchain.give_coins(ann, 3)

    blockchain.initialize_genesis_block()

    print("Ditributed coins:")
    john.checkout(blockchain)
    bob.checkout(blockchain)
    ann.checkout(blockchain)
    print("")

    # case 1 - single coin transactions
    print("Case 1:")
    john.checkout(blockchain)
    bob.checkout(blockchain)
    john.request_transaction(bob.name, [0], blockchain)
    john.request_transaction(bob.name, [1], blockchain)
    john.checkout(blockchain)
    bob.checkout(blockchain)
    bob.request_transaction(ann.name, [1], blockchain)
    bob.checkout(blockchain)
    ann.checkout(blockchain)
    print("")

    # case 2 - multiple coins transactions
    print("Case 2:")
    bob.request_transaction(john.name, [2, 3], blockchain)
    john.checkout(blockchain)
    bob.checkout(blockchain)
    print("")

    # case 3 - double spending in single coin transactions
    print("Case 3:")
    ann.checkout(blockchain)
    ann.request_transaction(john.name, [1], blockchain)
    ann.checkout(blockchain)
    ann.request_transaction(john.name, [1], blockchain)
    print("")

    # case 4 - double spending in multiple coins transactions
    print("Case 4:")
    ann.request_transaction(john.name, [4, 5], blockchain)
    ann.checkout(blockchain)
    ann.request_transaction(john.name, [4, 6], blockchain)
    print("")

    # blockchain validation
    print("Blockchain validation:")
    bob.validate_blockchain(blockchain)
    ann.validate_blockchain(blockchain)
    john.validate_blockchain(blockchain)
    bob.validate_coins(blockchain)
    ann.validate_coins(blockchain)
    john.validate_coins(blockchain)


    # print whole blockchain
    print("Blockchain:")
    blockchain.show_chain()

if __name__ == "__main__":
    main()
